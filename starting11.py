from bs4 import BeautifulSoup
import nltk
import re

class Events:
	def __init__(self, time, highlight, data):
		self.t = time
		self.hl = highlight
		self.d = data


html_doc = open("commentary.html", "r")

soup = BeautifulSoup(html_doc)

html_doc.close()

listData = soup.find('ol', {'class' : 'v5-timeline-list timeline-list-t3'})

listData = listData.find_all("li")
listData.reverse()

matchData = []

p = re.compile('.:.')

for i in listData:
	time = i.find(class_ = 'time')
	#print str(i.contents) + '\n'
	data = i.find('p')
	data = data.contents
	words = nltk.word_tokenize(str(data))
	info = nltk.pos_tag(words)
	print info
	print "\n"
	if str(time.contents) == "[]" or p.match(str(time.contents)):
		listData.remove(i)
		continue
	else:
		data = i.find('p')
		data = data.contents
		highlight = i.attrs["class"]
		
		current = Events(time.contents[0], highlight[0], data[0])
		matchData.append(current)