### Basic Prompt for colab:

`Write Python code for Colab that shows the next three buses from Wellington Station or Lambton Quay North to Te Herenga Waka – Victoria University of Wellington Kelburn, using the Metlink Open Data API. Read my API key with google.colab.userdata.get('METLINK_API_KEY'), see the first cell in this notebook.`
`Kelburn is not the last stop, so check each trip's stop times to confirm it calls there.`

### Refined Prompt for creating the:

```text
Write Python code for Google Colab to display the next three buses traveling from Wellington Station or Lambton Quay North to the Te Herenga Waka – Victoria University of Wellington Kelburn Campus using the Metlink Open Data API.

Requirements:
1. Read the Metlink API key using: google.colab.userdata.get('METLINK_API_KEY')
2. Since Kelburn is not the final stop for most of these routes, download and extract the static GTFS feed (https://static.opendata.metlink.org.nz/v1/gtfs/full.zip) to map valid active trips (trip_ids) where an origin stop sequence is less than a destination stop sequence.
3. Call the stop predictions API (https://api.opendata.metlink.org.nz/v1/stop-predictions?stop_id=...) for the origin stops. Ensure you parse the nested JSON correctly (e.g., getting departure expected/aimed times from inside the 'departure' or 'arrival' sub-objects, trip_id from 'trip', and route_short_name from 'service').
4. Filter the live predictions by comparing them to your mapped GTFS trip_ids or matched routes, sort them chronologically, and output the next three upcoming departures in local Wellington time.
```

