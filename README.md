# Diving Board

[HiDive](https://www.hidive.com) API wrapper built using [Get
Around](https://github.com/ryn-cx/get-around).

## Installation

```bash
uv add git+https://github.com/ryn-cx/diving-board
```

## Usage

The client holds one attribute per endpoint. Calling it downloads the file and
reads it into its model, and `download` and `load` are the two halves of that.

```python
from diving_board import DivingBoard

client = DivingBoard()

series = client.series(2311)
season = client.season(24579)
vod = client.vod(655773)
search = client.search("2.5 Dimensional Seduction")
adjacent = client.adjacent_series(2311, 24579)
schedule = client.schedule()

downloaded = client.series.download(2311)
series = client.series.load(downloaded)
```

The schedule is paged, and one call is one page. The page that comes back says
what the next one is asked for:

```python
pages = client.schedule.download_all()
schedules = client.schedule.load_pages(pages)
```
