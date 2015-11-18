import urllib
from BeautifulSoup import *

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_201026.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')

comments = soup('span')
sum_comments = 0
for comment in comments:
   # Look at the parts of a tag
   print 'TAG:',comment.contents[0]
   #print 'URL:',tag.get('href', None)
   #print 'Contents:',tag.contents[0]
   #print 'Attrs:',tag.attrs
   sum_comments +=  int(comment.contents[0])

print sum_comments
