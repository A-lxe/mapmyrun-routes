import sys
import os
import time
import json
import pprint
import requests

def writeRouteFiles(jsonMeta, textGpx, dir='./out'):
    dir = dir + '/' + jsonMeta['_links']['self'][0]['id']
    if not os.path.exists(dir): os.makedirs(dir)
    pp = pprint.PrettyPrinter(indent=4)
    jsonFile = open(dir + '/meta.json', 'w')
    jsonFile.write(pp.pformat(jsonMeta))
    jsonFile.close()
    gpxFile = open(dir + '/route.gpx', 'w')
    gpxFile.write(textGpx)
    gpxFile.close()

url = 'https://oauth2-api.mapmyapi.com'

key = sys.argv[1]
secret = sys.argv[2]
limit = int(sys.argv[5])

query = dict()
query['close_to_location'] = sys.argv[3]
query['search_radius'] = int(sys.argv[4])

headers = dict()
headers['api-key'] = key
headers['authorization'] = 'Bearer ' + secret
headers['content-type'] = 'application/json'

i = 0
while(limit == -1 or i < limit):
    print 'Offset: ' + str(i)
    time.sleep(1)
    query['offset'] = i
    req = requests.get(url + '/v7.1/route/',
                       params=query,
                       headers=headers)
    reqJson = req.json()
    if i >= reqJson['total_count']: break
    for route in reqJson['_embedded']['routes']:
        i += 1
        routeUrl = route['_links']['alternate'][1]['href']
        routeReq = requests.get(url + routeUrl,
                                headers=headers)
        print routeReq.reason
        print "Writing route " + route['_links']['self'][0]['id']
        writeRouteFiles(route, routeReq.text)

print "Complete!"
