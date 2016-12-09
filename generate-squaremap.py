import gpxpy
import gpxpy.gpx
import sys
import os
import csv

squareWidth = sys.argv[1]
directory = sys.argv[2]
csvFilename = "route-frequencymap.csv"

squareMap = {}

for filename in os.listdir(directory):
    gpxFile = open(directory + "/" + filename, 'r')
    gpx = gpxpy.parse(gpxFile)

    for track in gpx.tracks: 
        for segment in track.segments: 
            for point in segment.points: 
                print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)
                point = (point.latitude - point.latitude % squareWidth, point.longitude - point.longitude % squareWidth)
                squareMap[point] = 1 + squareMap[point] if squareMap.has_key(point) else 1


with open(csvFilename, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['latitude', 'longitude', 'frequency'])
for entry in squareMap.items():
            writer.writerow([entry[0][0], entry[0][1], entry[1]])
