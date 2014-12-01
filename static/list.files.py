import json
from pprint import pprint
json_data=open('places.json')

data = json.load(json_data)
#pprint(data['features'][1]['properties']['id'])

placelist = open('placelist.txt','wt')

for feature in data['features']:
	id = feature['properties']['id'] + "\n"
	pprint(id)
	placelist.write(id)
	
json_data.close()