'''

1.ISBT                          (28.673471,77.22853)    ()
2.Delhi gate                    (28.643055,77.238249)   (546m)
3.ITO                           (28.6293713,77.2391261) (750m)
4.Ashram                        (28.574984,77.262073)   ()
5.AIIMS                         (28.5671774,77.2078516) (260m)
6.Dhaula Kuan                   (28.5975268,77.1619938) (1km)
7.Naraina                       (28.621133,77.1326956)  (1.5km)
8.Raja Garden                   (28.645957,77.124602)   (1km)
9.Punjabi Bagh                  (28.666194,77.134033)   (460m)
10.Azadpur                      (28.707711,77.1774568)  (1.8km)
11.Mall Road(Delhi University)  (28.6947212,77.2124089) (731m)

'''



import urllib
import json
import time

site = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key=HiA2ysxthwHpirgLzFrUJQOQDkhR3a1x&point="
location = raw_input("Enter the lat and longitude of the place(comma separated value): ")
url = site + location

place = raw_input("Enter the name of the place: ")

response = urllib.urlopen(url)
data = json.load(response)

road_type = data["flowSegmentData"]["frc"]
current_time = data["flowSegmentData"]["currentTravelTime"]
current_speed = data["flowSegmentData"]["currentSpeed"]
free_flow_time = data["flowSegmentData"]["freeFlowTravelTime"]
free_flow_speed = data["flowSegmentData"]["freeFlowSpeed"]
coordinates = data["flowSegmentData"]["coordinates"]["coordinate"]

#print(data)

'''
print(road_type)
print(current_time)
print(current_speed)
print(free_flow_time)
print(free_flow_speed)
'''

def write_to_file(coordinates):
    f = open(place, "a+")
    for i in range(len(coordinates)):
        f.write(str(coordinates[i]["latitude"]) + " , " + str(coordinates[i]["longitude"]) + "\n")
    f.close()
    print("Coordinates written to txt file successfully.")


write_to_file(coordinates)
