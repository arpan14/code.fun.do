import urllib2
from BeautifulSoup import BeautifulSoup
import re
import csv
import time

csvfile1 = open('MusicCSV.csv', 'rb')
d = {}
csvfile2 = open('artistWithURL.csv', 'wb')
artistList = []
writer = csv.writer(csvfile2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
reader = csv.reader(csvfile1, delimiter=',', quotechar='|')
row = next(reader)
for artist in row:
	artistList.append(artist)
for artist in artistList:
	status = [artist]
	time.sleep(1)
	temp = artist.replace(" ","+")
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]

	url = ('https://www.youtube.com/results?search_query=') + temp 
	ourUrl = opener.open(url).read()
	soup = BeautifulSoup(ourUrl)
	try:
		body = soup.find('button', attrs = {'aria-label' : 'Search filters'})
		if body != None:
			nextE = body.findNext('a', attrs = {'class' : re.compile('^yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis')})
			result = nextE['href']
			d[artist] = result
			status.append('Success')
	except:
		status.append('Failed')
		pass
	print status

for key, value in d.iteritems():
	row = [key, value]
	writer.writerow(row)