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
	print str(i.contents) + '\n'
	if str(time.contents) == "[]" or p.match(str(time.contents)):
		listData.remove(i)
		continue
	else:
		data = i.find('p')
		data = data.contents
		highlight = i.attrs["class"]
		
		current = Events(time.contents[0], highlight[0], data[0])
		matchData.append(current)

# for i in matchData:
# 	print i.t + " --> " + i.hl + "\n" + i.d + "\n\n"
# 	text = nltk.word_tokenize(i.d)
# 	info = nltk.pos_tag(text)
# 	for j in info:
# 		if j[1] == "NNP":
# 			print j[0] + " --> " + j[1]