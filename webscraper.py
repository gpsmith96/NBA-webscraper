from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time

browser = webdriver.PhantomJS("C:/Users/Graham/software ws/phantomjs-2.1.1-windows/bin/phantomjs.exe")

url = 'https://ca.global.nba.com/scores/?_ga=2.41354277.626674850.1553839244-663800549.1539826533'
browser.get(url)
dataArr = []
while True:
	content = BeautifulSoup(browser.page_source, "html.parser")
	gameArr = []
	gameData = {
		"date": content.find('span', attrs={"class": "day ng-binding"}).text,
		"data": gameArr,
	}
	for game in content.findAll('table', attrs={"class": "final-game-table"}):
		gameObject = {
			"awayScore": int(game.findAll('td', attrs={"class": "final-score"})[0].text),
			"homeScore": int(game.findAll('td', attrs={"class": "final-score"})[1].text),
			"awayTeam": game.findAll('td', attrs={"class": "team-abbrv"})[0].find('a').text,
			"homeTeam": game.findAll('td', attrs={"class": "team-abbrv"})[1].find('a').text,
		}
		gameArr.append(gameObject)
	print(gameData)
	dataArr.append(gameData)
	browser.find_element_by_class_name("icon-caret-left").click()
	if(gameData['date'] == 'Fri, Mar 01'):
		break
	time.sleep(2)





with open('gameData.json', 'w') as outfile:
	json.dump(dataArr, outfile)