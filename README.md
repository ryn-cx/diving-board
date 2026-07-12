# Diving Board

[HiDive](https://www.hidive.com) API wrapper built using [Good Ass Pydantic
Integrator](https://github.com/ryn-cx/good-ass-pydantic-integrator) and [Get
Around](https://github.com/ryn-cx/get-around).

## Installation

```bash
uv add git+https://github.com/ryn-cx/diving-board
```

## Usage

Every endpoint has `get()` (parsed, typed model) and `download()` (raw JSON).

```python
from diving_board import DivingBoard

client = DivingBoard()

series = client.series.get(series_id)
season = client.season.get(season_id)
vod = client.vod.get(vod_id)
search = client.search.get(query)
adjacent_series_to = client.adjacent_series_to.get(series_id, season_id)
schedule = client.schedule.get()
```
