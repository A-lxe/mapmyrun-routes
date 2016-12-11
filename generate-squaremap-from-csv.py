import sys
import os
import csv

squareWidth = float(sys.argv[1])
inputFile = sys.argv[2]
x1 = sys.argv[3]
y1 = sys.argv[4]
x2 = sys.argv[5]
y2 = sys.argv[6]
csvFilename = "pedestrian-frequencymap.csv"

squareMap = {}

csvfile = open(inputFile, 'r')
reader = csv.reader(inputfile, delimiter=',', quotechar='|')



counter = 0;
for filename in os.listdir(directory):
    if counter % 10 == 0: print("Files Read: {0}".format(counter))
    gpxFile = open(directory + "/" + filename, 'r')
    try:
        gpx = gpxpy.parse(gpxFile)

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    point = (point.latitude - point.latitude % squareWidth, point.longitude - point.longitude % squareWidth)
                    squareMap[point] = 1 + squareMap[point] if squareMap.has_key(point) else 1
            counter += 1
    except:
        print("Bad file: {0}".format(filename))
        pass

csvfile = open(csvFilename, 'wb')
writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer.writerow(['latitude', 'longitude', 'frequency'])
for entry in squareMap.items():
    writer.writerow([entry[0][0], entry[0][1], entry[1]])

csvfile.close()
