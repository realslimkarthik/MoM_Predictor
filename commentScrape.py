import urllib2
from bs4 import BeautifulSoup, SoupStrainer
import nltk

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


class Events:
    def __init__(self, time, highlight, data):
        self.t = time
        self.hl = highlight
        self.d = data

link = "http://www1.skysports.com/football/live/match/279816/commentary/all"

response = urllib2.urlopen(link)
html_doc = response.read()

soup = BeautifulSoup(html_doc)

listData = soup.find('ol', {'class' : 'v5-timeline-list timeline-list-t3'})

listData = listData.find_all("li")
listData.reverse()

matchData = []

for i in listData:
    time = i.find(class_ = 'time')
    if str(time.contents) == "[]":
        listData.remove(i)
        continue
    else:
        data = i.find('p')
        data = data.contents
        highlight = i.attrs["class"]
        
        current = Events(time.contents[0], highlight[0], data[0])
        matchData.append(current)

for i in matchData:
    print i.t + " --> " + i.hl + "\n" + i.d + "\n\n"