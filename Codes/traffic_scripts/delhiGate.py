import urllib2
import json
import csv
import time
import datetime


def request_data_from_url(request_url):
    req = urllib2.Request(request_url)
    success = False
    while success == False:
        try:
            response = urllib2.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception, e:

            print e
            time.sleep(5)
            print("Error. Retrying...")

    return response.read()




"""
INPUTS:
    api_key: authentication to GMaps that we're allowed to request this data
    origin: lat,long of road
    frequency: how often to scrape the data
    duration: how long to scrape the data
OUTPUTS:
    nothing, simply continues to write data to spreadsheet
"""
def scrape_gmaps_data(frequency, duration):


    request_url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key=HiA2ysxthwHpirgLzFrUJQOQDkhR3a1x&point=28.643055,77.238249"

    with open("delhiGate_trafficData.csv", 'a') as file:
        #let w represent our file
        w = csv.writer(file)

        #write the header row
        w.writerow(["timestamp", "Road Type", "Free Flow Time(seconds)", "Free Flow Speed(KMPH)", "Current Time(seconds)", "Current Speed(KMPH)"])

        #get the travel time at regular intervals
        step = 1
        while (step <= int(duration*60 / frequency)):
            #convert response to python dictionary
            data = json.loads(request_data_from_url(request_url))

            #extract relevant data from response
            road_type = data["flowSegmentData"]["frc"]
            current_time = data["flowSegmentData"]["currentTravelTime"]
            current_speed = data["flowSegmentData"]["currentSpeed"]
            free_flow_time = data["flowSegmentData"]["freeFlowTravelTime"]
            free_flow_speed = data["flowSegmentData"]["freeFlowSpeed"]


            #write to our spreadsheet
            w.writerow((datetime.datetime.now(), road_type, free_flow_time, free_flow_speed, current_time, current_speed))
            if step % 10 == 0:
                print str(step) + ' datapoints gathered ...'

            step += 1
            time.sleep(frequency*60)
        print("Data written successfully!!")




if __name__ == '__main__':
    scrape_gmaps_data(15, 4)
