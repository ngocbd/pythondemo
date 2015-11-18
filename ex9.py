import urllib
from BeautifulSoup import *

url = " http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Diaz.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')

repeat = 7
position = 18

for i in range (0,repeat):
    nexturl=tags[position-1].get('href', None)
    #print nexturl
    html = urllib.urlopen(nexturl).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
print nexturl