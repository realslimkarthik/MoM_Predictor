from bs4 import BeautifulSoup
import nltk
import nltk.data
import re
import json

class Events:
    def __init__(self, time, highlight, data):
        self.t = time
        self.hl = highlight
        self.d = data

html_doc = open("commentary.html", "r")

soup = BeautifulSoup(html_doc)

html_doc.close()

json_data = open("teams.json", "r")
teams = json.load(json_data)

listData = soup.find('ol', {'class' : 'v5-timeline-list timeline-list-t3'})

listData = listData.find_all("li")
listData.reverse()

matchData = []

p = re.compile('.:.')

for i in listData:
    time = i.find(class_ = 'time')
    #print str(i.contents) + '\n'
    if str(time.contents) == "[]" or p.match(str(time.contents)):
        listData.remove(i)
        continue
    else:
        data = i.find('p')
        data = data.contents
        highlight = i.attrs["class"]
        
        current = Events(time.contents[0], highlight[0], data[0])
        matchData.append(current)

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

for i in matchData:
    print i.t #+ " --> " + i.hl + "\n" + i.d + "\n\n"
    sent = sent_detector.tokenize(i.d)
    for j in sent:
    	print j
        text = nltk.word_tokenize(j)
        info = nltk.pos_tag(text)
        for k in info:
            if k[1] == "NNP" and k[0] in teams['Chelsea'] or k[0] in teams['Arsenal']:
                print k[0] + " --> " + k[1]
            if k[1] == "VB" or k[1] == "VBP" or k[1] == "VBD" or k[1] == "VBG" or k[1] == "VBN":
            	print k[0] + " --> " + k[1]