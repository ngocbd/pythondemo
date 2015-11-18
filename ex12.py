import json
import urllib
#http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Zagazig%20University
location = raw_input("Enter Location")
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/geojson?sensor=false&"+urllib.urlencode({'address':location})
data = urllib.urlopen(url).read()



info = json.loads(data)


for item in info["results"]:
   print item['place_id']

