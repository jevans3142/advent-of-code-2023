import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

races = []

timesraw = f.readline().split(":")[1].split()
distancesraw = f.readline().split(":")[1].split()

for idx, timeraw in enumerate(timesraw):
    races.append({"time":int(timeraw), "distance":int(distancesraw[idx])})

ways_to_beat_product = 1 

for race in races: 
    ways_to_beat_this_race = 0
    for test_time in range(1,race["time"]):
        speed = test_time # in mm per second
        distance_travelled = speed * (race["time"]-test_time)
        if distance_travelled>race["distance"]:
            # This beats the record
            ways_to_beat_this_race += 1

    ways_to_beat_product = ways_to_beat_product * ways_to_beat_this_race

print("The product of the ways to beat each record is : " + str(ways_to_beat_product))