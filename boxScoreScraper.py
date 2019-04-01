from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import json
import datetime
import time

def scrape_box_score(page):
	content = BeautifulSoup(page.page_source, "html.parser")
	teams = content.findAll('nba-stat-table')
	teamnames = content.findAll('div', attrs={'class':'nba-stat-table__caption'})
	AwayTeamStats=[]
	AwayTeamData = {
		'Name': teamnames[0].text,
		'Data': AwayTeamStats,
	}
	HomeTeamStats=[]
	HomeTeamData = {
		'Name': teamnames[1].text,
		'Data': HomeTeamStats,
	}

	for player in teams[0].find('tbody').findAll('tr'):
		stats = player.findAll('td')
		if (stats[1].text != ''):
			playerStats = {
				'Name': stats[0].text,
				'seconds': stats[1].text,
				'FGM': int(stats[2].text),
				'FGA': int(stats[3].text),
				'3PM': int(stats[5].text),
				'3PA': int(stats[6].text),
				'FTM': int(stats[8].text),
				'FTA': int(stats[9].text),
				'OREB': int(stats[11].text),
				'DREB': int(stats[12].text),
				'TREB': int(stats[13].text),
				'AST': int(stats[14].text),
				'TOV': int(stats[15].text),
				'STL': int(stats[16].text),
				'BLK': int(stats[17].text),
				'PF': int(stats[18].text),
				'PTS': int(stats[19].text),
				'+-': int(stats[20].text),
			}
		else:
			playerStats = {
				'Name': stats[0].text,
				'seconds': stats[2].text,
				'FGM': 0,
				'FGA': 0,
				'3PM': 0,
				'3PA': 0,
				'FTM': 0,
				'FTA': 0,
				'OREB': 0,
				'DREB': 0,
				'TREB': 0,
				'AST': 0,
				'TOV': 0,
				'STL': 0,
				'BLK': 0,
				'PF': 0,
				'PTS': 0,
				'+-': 0,
			}
		AwayTeamStats.append(playerStats)
	for player in teams[1].find('tbody').findAll('tr'):
		stats = player.findAll('td')
		if (stats[1].text != ''):
			playerStats = {
				'Name': stats[0].text,
				'seconds': stats[1].text,
				'FGM': int(stats[2].text),
				'FGA': int(stats[3].text),
				'3PM': int(stats[5].text),
				'3PA': int(stats[6].text),
				'FTM': int(stats[8].text),
				'FTA': int(stats[9].text),
				'OREB': int(stats[11].text),
				'DREB': int(stats[12].text),
				'TREB': int(stats[13].text),
				'AST': int(stats[14].text),
				'TOV': int(stats[15].text),
				'STL': int(stats[16].text),
				'BLK': int(stats[17].text),
				'PF': int(stats[18].text),
				'PTS': int(stats[19].text),
				'+-': int(stats[20].text),
			}
		else:
			playerStats = {
				'Name': stats[0].text,
				'seconds': stats[2].text,
				'FGM': 0,
				'FGA': 0,
				'3PM': 0,
				'3PA': 0,
				'FTM': 0,
				'FTA': 0,
				'OREB': 0,
				'DREB': 0,
				'TREB': 0,
				'AST': 0,
				'TOV': 0,
				'STL': 0,
				'BLK': 0,
				'PF': 0,
				'PTS': 0,
				'+-': 0,
			}
		HomeTeamStats.append(playerStats)


	GameData = [AwayTeamData, HomeTeamData]
	#print(GameData)
	return(GameData)





chromeOptions = Options()
#chromeOptions.add_argument('--headless')
gamedate = datetime.date(2018, 10, 16)
driver = webdriver.Chrome(options = chromeOptions)
baseurl='https://stats.nba.com'
Data=[]	
while gamedate < datetime.date.today():
	textdate = str(gamedate.month) + '/' + str(gamedate.day) + "/" + str(gamedate.year)
	url = 'https://stats.nba.com/scores/' + textdate
	driver.get(url)
	content = BeautifulSoup(driver.page_source, "html.parser")

	for button in content.findAll('div', attrs={'class':'bottom-bar hide-for-pre-game'}):
		driver.get(baseurl + button.find('a').get('href'))
		time.sleep(1)
		GameData = {
			'date': textdate,
			'data': scrape_box_score(driver),
		}
		Data.append(GameData)
	gamedate = gamedate + datetime.timedelta(1)

	
print(Data)

with open('boxScoreData.json', 'w') as outfile:
	json.dump(Data, outfile)
#driver.quit()