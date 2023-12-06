import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

races = []

time = int(f.readline().split(":")[1].replace(" ", ""))
distance = int(f.readline().split(":")[1].replace(" ", ""))


ways_to_beat_this_race = 0
for test_time in range(1, time):
    speed = test_time  # in mm per second
    distance_travelled = speed * (time - test_time)
    if distance_travelled > distance:
        # This beats the record
        ways_to_beat_this_race += 1

print("The number of ways to beat the record is : " + str(ways_to_beat_this_race))
