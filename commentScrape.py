import urllib2
from bs4 import BeautifulSoup, SoupStrainer

link = "http://www1.skysports.com/football/live/match/279816/commentary/all"

response = urllib2.urlopen(link)
html_doc = response.read()

soup = BeautifulSoup(html_doc)

listData = soup.find_all(class_ = 'v5-timeline-list timeline-list-t3')

print listData