#!/usr/bin/env python3
"""Next buses from Wellington Station / Lambton Quay North to VUW Kelburn.

Uses the Metlink Open Data API (https://opendata.metlink.org.nz).
The API key is read from metlink_key.txt next to this script.

Usage:  python3 next_bus.py [-n 3]
"""

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

import requests

BASE = "https://api.opendata.metlink.org.nz/v1"
ORIGIN_PREFIXES = ("Wellington Station - ", "Lambton Quay North - ")
DEST_MATCH = "Victoria University of Wellington Kelburn"


def load_key():
    path = Path(__file__).resolve().parent / "metlink_key.txt"
    try:
        key = path.read_text().strip()
    except FileNotFoundError:
        sys.exit(f"API key not found: {path}")
    if not key:
        sys.exit(f"API key file is empty: {path}")
    return key


class Metlink:
    def __init__(self, key):
        self.session = requests.Session()
        self.session.headers["x-api-key"] = key

    def get(self, endpoint, **params):
        r = self.session.get(f"{BASE}/{endpoint}", params=params, timeout=20)
        r.raise_for_status()
        return r.json()

    def departures(self, stop_id):
        return self.get("stop-predictions", stop_id=stop_id).get("departures", [])

    def stop_times(self, trip_id):
        return self.get("gtfs/stop_times", trip_id=trip_id)


def dep_time(dep):
    """Best departure time: real-time estimate if available, else timetable."""
    d = dep.get("departure") or {}
    a = dep.get("arrival") or {}
    expected = d.get("expected") or a.get("expected")
    aimed = d.get("aimed") or a.get("aimed")
    ts = expected or aimed
    return (datetime.fromisoformat(ts), expected is not None) if ts else (None, False)


def short(name):
    return name.replace("Te Herenga Waka – Victoria University of Wellington ", "")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("-n", "--count", type=int, default=3, help="number of buses (default 3)")
    args = ap.parse_args()

    api = Metlink(load_key())

    # 1. Find stops by name.
    stops = api.get("gtfs/stops")
    names = {s["stop_id"]: s["stop_name"] for s in stops}
    origins = [s["stop_id"] for s in stops if s["stop_name"].startswith(ORIGIN_PREFIXES)]
    dests = {s["stop_id"] for s in stops if DEST_MATCH in s["stop_name"]}
    if not origins or not dests:
        sys.exit("Could not find the origin or destination stops in the Metlink stop list.")

    # 2. Live departures at every origin stop, plus routes seen at Kelburn.
    with ThreadPoolExecutor(max_workers=8) as pool:
        origin_deps = list(pool.map(api.departures, origins))
        dest_deps = list(pool.map(api.departures, sorted(dests)))
    kelburn_routes = {d["service_id"] for deps in dest_deps for d in deps}

    now = datetime.now().astimezone()
    candidates = []
    for deps in origin_deps:
        for d in deps:
            when, realtime = dep_time(d)
            if when and when >= now and d.get("trip_id") and d["service_id"] in kelburn_routes:
                candidates.append((when, realtime, d))
    candidates.sort(key=lambda c: c[0])

    # 3. Confirm each trip calls at Kelburn *after* the boarding stop.
    trip_cache = {}

    def calls_kelburn(dep):
        trip = dep["trip_id"]
        if trip not in trip_cache:
            trip_cache[trip] = api.stop_times(trip)
        seq = {st["stop_id"]: int(st["stop_sequence"]) for st in trip_cache[trip]}
        board = seq.get(dep["stop_id"])
        if board is None:
            return None
        after = [s for s in dests if seq.get(s, -1) > board]
        return after[0] if after else None

    results = []
    for when, realtime, dep in candidates:
        dest = calls_kelburn(dep)
        if dest:
            results.append((when, realtime, dep, dest))
            if len(results) == args.count:
                break

    # 4. Print.
    print("Next buses to Te Herenga Waka – VUW Kelburn")
    print(f"(as of {now:%H:%M:%S})\n")
    if not results:
        print("No upcoming buses found right now. Try again later.")
        return
    for when, realtime, dep, dest in results:
        mins = max(0, round((when - now).total_seconds() / 60))
        tag = "live" if realtime else "scheduled"
        print(f"{when:%H:%M}  in {mins:>2} min  {tag:<9}  Route {dep['service_id']:<4}"
              f" from {names.get(dep['stop_id'], dep['stop_id'])}"
              f"  →  {short(names[dest])}   [to {dep.get('trip_headsign', '?')}]")


if __name__ == "__main__":
    try:
        main()
    except requests.RequestException as e:
        sys.exit(f"Metlink API error: {e}")
