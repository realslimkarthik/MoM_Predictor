from bs4 import BeautifulSoup
import nltk
import urllib2
import json

# For future Use
# class Player:
#     def __init__(self, team, player, rating, position):
#         self.t = team
#         self.p = player
#         self.r = rating
#         self.pos = position


def getTeam(link):
    response = urllib2.urlopen(link)
    html_doc = response.read()

    soup = BeautifulSoup(html_doc)

    listData = soup.find_all('ul', {'class' : 'sq-lst'})

    hLineup = soup.find('a', {'href': '#teamlineup-homeTeam'})
    aLineup = soup.find('a', {'href': '#teamlineup-awayTeam'})
    home = str(hLineup.contents[0].strip())
    away = str(aLineup.contents[0].strip())
    teams[home] = []
    teams[away] = []

    listH = listData[1].find_all('li')
    listHS = listData[2].find_all('li')
    listH += listHS

    for i in listH:
        sp = i.find_all("span")
        pl = sp[1].contents
        teams[home].append(str(pl[0].strip()))

    listA = listData[4].find_all('li')
    listAS = listData[5].find_all('li')
    listA += listHS

    for i in listA:
        sp = i.find_all("span")
        pl = sp[1].contents
        teams[away].append(str(pl[0].strip()))
    return teams
            


if __name__=="__main__":
    #link = 'http://www1.skysports.com/football/live/match/279816/teams'
    link = 'http://www1.skysports.com/football/live/match/313388/teams'
    teams = getTeam(link)
    with open('teams.json', 'w') as outfile:
        json.dump(teams, outfile)
