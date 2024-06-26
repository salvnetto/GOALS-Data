import requests
import pandas as pd
from bs4 import BeautifulSoup


def getTeamsUrl(url) -> list:
    data = requests.get(url)
    soup = BeautifulSoup(data.text, features='lxml')
    table = soup.select('table.stats_table')[0]
    links = table.find_all('a')
    links = [link.get('href') for link in links]
    links = [link for link in links if '/squads/' in link]
    urls = [f"https://fbref.com{link}" for link in links]

    return urls


def renameColumns(columns) -> list:
    column_counts = {}
    new_column_names = []

    for column in columns:
        if column not in column_counts:
            column_counts[column] = 1
            new_column_names.append(column)
        else:
            column_counts[column] += 1
            new_column_names.append(f"{column}_90")

    return new_column_names


def addTeamMetadata(teamFile, season, teamUrl, leagueName, leagueId) -> pd.DataFrame:
    teamFile['season'] = season
    teamFile['league_name'] = leagueName
    teamFile['league_id'] = leagueId
    teamName = teamUrl.split('/')[-1].replace('-Stats', '').replace('-', '_').lower()
    teamFile['team_name'] = teamName
    teamId = teamUrl.split('/')[5]
    teamFile['team_id'] = teamId

    print(f'--{teamName}')
    return teamFile
