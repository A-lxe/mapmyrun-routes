import sys
import json
import pprint
import requests

url = 'https://oauth2-api.mapmyapi.com'

key = sys.argv[1]
secret = sys.argv[2]

query = dict()
query['close_to_location'] = sys.argv[3]
query['search_radius'] = int(sys.argv[4])

headers = dict()
headers['api-key'] = key
headers['authorization'] = 'Bearer ' + secret
headers['content-type'] = 'application/json'

req = requests.get(url + '/v7.1/route/',
                   params=query,
                   headers=headers)

tmp = req.json()['_embedded']['routes'][0]['_links']['alternate'][1]['href']
req2 = requests.get(url + tmp,
                    headers=headers)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(req2.text)

print req.status_code
print req.reason
