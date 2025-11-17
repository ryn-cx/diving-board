<div align="center">

# 🏊 Diving Board

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/ryn-cx/diving-board/refs/heads/master/pyproject.toml)
![GitHub License](https://img.shields.io/github/license/ryn-cx/diving-board)
![GitHub Issues](https://img.shields.io/github/issues/ryn-cx/diving-board)

**An unofficial Python API client for HiDive**

</div>

## ✨ Features

- 🔑 **Automatic Authentication**: Handles API key extraction and multi-layer authorization automatically
- 🛡️ **Type Safety**: Full Pydantic models for every endpoint
- 🔄 **Dynamically Updating Models**: Models are dynamically updated based on the response from the API

## 📦 Installation

### Requirements

- 🐍 Python 3.13 or higher

### Install from source

```bash
uv add git+https://github.com/ryn-cx/diving-board
```

## 🚀 Quick Start

### Create Client

```python
from diving_board import DivingBoard

# 🌐 Create client
client = DivingBoard()
```

### Access API

```python
# 📺 Get season information
season = client.get_season(18914)

# 📋 Get other seasons for a show
other_seasons = client.get_other_seasons(series_id=1081, season_id=19337)
```
