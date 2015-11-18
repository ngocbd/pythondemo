import json
import urllib
#http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Zagazig%20University
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_201027.json"
data = urllib.urlopen(url).read()



info = json.loads(data)

total = 0
for item in info["comments"]:
    total+=item['count']

print total