import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

seeds = []
seed_to_soil_map = []
soil_to_fert_map = []
fert_to_water_map = []
water_to_light_map = []
light_to_temp_map = []
temp_to_humd_map = []
humd_to_location_map = []

areas_of_file = [seeds, seed_to_soil_map,soil_to_fert_map,fert_to_water_map,water_to_light_map,light_to_temp_map,temp_to_humd_map,humd_to_location_map]


def use_map(map, input):
    for map_item in map: 
        if input in range(map_item[1],map_item[1]+map_item[2]):
            return map_item[0] + (input-map_item[1])
    return input

area_of_file_currently = 0

for line in f:

    # First we need to special case handle the seeds
    if (area_of_file_currently == 0 and seeds ==[]):
        seeds_temp = line.split(":")[1].split()
        for x in seeds_temp:
            seeds.append(int(x))
        continue

    if line == "\n": # First check for moving between areas 
        area_of_file_currently += 1 
        continue

    if line.find(":") != -1:
        # Check if it's a title line we should skip
        continue

    dest_rng_start = int(line.split()[0])
    src_rng_start = int(line.split()[1])
    rng_length = int(line.split()[2])

    areas_of_file[area_of_file_currently].append([dest_rng_start, src_rng_start, rng_length])

locations = []

for seed in seeds:
    soil = use_map(seed_to_soil_map,seed)
    fert = use_map(soil_to_fert_map, soil)
    water = use_map(fert_to_water_map, fert)
    light = use_map(water_to_light_map, water)
    temp = use_map(light_to_temp_map, light)
    humd = use_map(temp_to_humd_map, temp)
    location = use_map(humd_to_location_map, humd)
    locations.append(location)

locations.sort()
print("The lowest location is : " + str(locations[0]))