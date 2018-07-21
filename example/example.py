#http://kevincsong.com/Scraping-stats.nba.com-with-python/
from selenium.webdriver import Chrome
from pandas import DataFrame

seasonEndYear = 2017
seasonTypeIndex = 2 # pre, reg, post, allstar
perModeIndex = 2 #totals, perGame, perMinute
rowPerPageIndex = 1 #Select All = 1

seasonIndex = 2019 - seasonEndYear


path_to_chromedriver = '/Users/footballnerd12/Desktop/Python/chromedriver' # Path to access a chrome driver
browser = Chrome(executable_path=path_to_chromedriver)

url = 'https://stats.nba.com/leaders'
browser.get(url)

xpath = '/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/label/select/option[' + str(seasonIndex) + ']'
browser.find_element_by_xpath(xpath).click()

xpath = '/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/label/select/option[' + str(seasonTypeIndex) + ']'
browser.find_element_by_xpath(xpath).click()

xpath = '/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/select/option[' + str(rowPerPageIndex) + "]"
browser.find_element_by_xpath(xpath).click()

table = browser.find_element_by_class_name('nba-stat-table__overflow')

player_ids = []
player_names = []
player_stats = []

for line_id, lines in enumerate(table.text.split('\n')):
    if line_id == 0:
        column_names = lines.split(' ')[1:]
    elif line_id % 3 == 1:
        player_ids.append(lines)
    elif line_id % 3 == 2:
        player_names.append(lines)
    elif line_id % 3 == 0:
        player_stats.append( [float(i) for i in lines.split(' ')] )

browser.close()
print()

db = DataFrame({'player': player_names,
                       'gp': [i[0] for i in player_stats],
                       'min': [i[1] for i in player_stats],
                       'pts': [i[2] for i in player_stats],
                       'fgm': [i[3] for i in player_stats], 
                       'fga': [i[4] for i in player_stats],
                       'fg%': [i[5] for i in player_stats],
                       '3pm': [i[6] for i in player_stats],
                       '3pa': [i[7] for i in player_stats],
                       '3p%': [i[8] for i in player_stats],
                       'ftm': [i[9] for i in player_stats],
                       'fta': [i[10] for i in player_stats],
                       'ft%': [i[11] for i in player_stats],
                       'oreb': [i[12] for i in player_stats],
                       'dreb': [i[13] for i in player_stats],
                       'reb': [i[14] for i in player_stats],
                       'ast': [i[15] for i in player_stats],
                       'stl': [i[16] for i in player_stats],
                       'blk': [i[17] for i in player_stats],
                       'tov': [i[18] for i in player_stats],
                       'eff': [i[19] for i in player_stats]
                       }
                     )
"""One annoying thing is that all the column names are getting re-ordered in alphabetical order. 
So we're going to reorder this by the following line:"""

db = db[['player', 'gp', 'min', 'pts', 'fgm', 'fga', 'fg%', '3pm', 
         '3pa', '3p%', 'ftm','fta', 'ft%', 'oreb', 'dreb','reb',
         'ast','stl','blk','tov','eff']]




print(db.to_string())


