import urllib2
from bs4 import BeautifulSoup, SoupStrainer

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