from .constants import URL_FBREF


class League:
    def __init__(self, countryCode):
        self.countryCode = countryCode
        self._setLeagueProperties()
      
    def _setLeagueProperties(self) -> None: 
        leagues = {
            'br': ('brasileirao', '24', 'full_year', 'Série A'),
            'en': ('premier_league', '9', 'split_years', 'Premier League'),
            'it': ('serie_a', '11', 'split_years', 'Serie A'),
            'es': ('la_liga', '12', 'split_years', 'La Liga'),
            'de': ('bundesliga', '20', 'split_years', 'Bundesliga'),
            'fr': ('ligue_1', '13', 'split_years', 'Ligue 1')
        }

        if self.countryCode in leagues:
            self.name, self.id, self.seasonType, self.FBREFCompName = leagues[self.countryCode]

            _urlName = self.name.replace('_','-').title()
            self.url = f"{URL_FBREF}/en/comps/{self.id}/season_placeholder/season_placeholder-{_urlName}-Stats"

            self.path = f"datasets/raw_data/{self.name}/"
        else:
            raise ValueError(f"Country Code '{self.countryCode}' not supported.")