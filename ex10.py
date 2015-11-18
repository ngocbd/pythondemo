import urllib
import xml.etree.ElementTree as ET

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_201023.xml '
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total = 0
for count in counts:
    total+=int( count.text)
print total