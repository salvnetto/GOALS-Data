# GOALS-Data

## Overview

The `GOALS-Data` repository serves as a supplementary data source for the `GOALS` package, providing access to raw and processed football data from various leagues and competitions. Leveraging web scraping techniques, the data is extracted from [fbref.com](https://fbref.com) and curated to ensure high quality. This repository aims to facilitate easy access to comprehensive football datasets for analysis and research purposes.

## Features

- Comprehensive data for multiple football leagues:
  - English Premier League
  - Brasileirão
  - Ligue 1
  - Serie A
  - La Liga
  - Bundesliga
- Includes match history, league standings, and team squads.

## Usage

Utilize the `loadData` function from the `GOALS` package to access the data from the `GOALS-Data` repository.

### Example: Loading Data with GOALS Package

```python
from goals import loadData

# Load processed match history data for Brasileirão
df = loadData('br', 'match_history')
print(df.head())

# Load raw standings data for the Premier League
df = loadData('en', 'standings', raw=True)
print(df.head())
```

For more details, visit the [GOALS GitHub repository](https://github.com/seu-usuario/nome-do-repositorio).
