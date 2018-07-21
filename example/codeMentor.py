#https://nbviewer.jupyter.org/github/practicallypredictable/posts/blob/master/basketball/nba/notebooks/scrape-stats_nba-team_matchups.ipynb
from time import sleep
import requests

def scrape_teamgamelogs(season, season_type, sleep_for=None):
    """Process JSON from stats.nba.com teamgamelogs endpoint and return unformatted DataFrame."""
    if sleep_for:
        sleep(sleep_for) # be nice to server by sleeping if we are scraping inside a loop
    nba_params = {
        'LeagueID': "00",
        'Season': season,
        'SeasonType': season_type,
    }
    r = requests.get(
        NBA_URL,
        params=nba_params,
        headers={
    'user-agent': (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) ' +
    'AppleWebKit/537.36 (KHTML, like Gecko) ' +
    'Chrome/61.0.3163.100 Safari/537.36'
),
},
        allow_redirects=False,
        timeout=15,
    )
    r.raise_for_status()
    results = r.json()['resultSets'][0]
    headers = results['headers']
    rows = results['rowSet']
    return pd.DataFrame(rows, columns=headers)