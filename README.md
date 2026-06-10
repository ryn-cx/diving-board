# Diving Board

Unofficial [HiDive](https://www.hidive.com) API.

`diving-board` wraps HiDive's private web API and parses its raw JSON into typed
[Pydantic](https://docs.pydantic.dev/) models, giving you a small, structured API for
reading data about HiDive series, seasons, VODs, playlists, schedules, and search.

## Installation

```bash
uv add git+https://github.com/ryn-cx/diving-board
```

## Usage

Create a client, then call `get(...)` on an endpoint to download from HiDive and
get back a parsed, typed model.

```python
from diving_board import DivingBoard

client = DivingBoard()

# A series, by series ID.
series = client.series.get(1091)

# A season, by season ID.
season = client.season.get(19078)

# A single VOD, by VOD ID.
vod = client.vod.get(542391)

# A playlist, by playlist ID.
playlist = client.playlist.get(19078)

# Search, by query string.
results = client.search.get("frieren")

# Other series in the same franchise, by series ID and season ID.
adjacent = client.adjacent_series.get(1091, 19078)

# The release schedule. Defaults to the current month.
schedule = client.schedule.get()

# Every schedule page from a starting date up to a given end date.
from datetime import datetime

pages = client.schedule.get_until_datetime(
    from_=datetime(2026, 1, 1),
    end_datetime=datetime(2026, 6, 1),
)
```
