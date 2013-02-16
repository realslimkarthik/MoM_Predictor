import urllib2

link = "http://www1.skysports.com/football/live/match/279816/commentary/all"

response = urllib2.urlopen(link)
html_doc = response.read()

commentary = open("commentary.html", "w")
commentary.write(html_doc)
commentary.close()