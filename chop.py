

import csv
import time
import datetime
import sh

segments = 100



def convertTimestamp(tstamp):
    print datetime.datetime.fromtimestamp(int(tstamp))

convertTimestamp(time.time())



with open('tracks/exported_tracks.txt','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter = '\t' )
    rowCount = 0
    for row in tsvin:
        rowCount++
    print('rowCount: ' + str(rowCount))

    index = 0
    fileName = str(index) + '_life.csv'
    for row in range(rowCount):
        print(tsvin.row[1])
