import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

input_image = f.readlines()

def xor_strings(input1,input2):
    output = ""
    for idx, char in enumerate(input1):
        if input1[idx] == "." and input2[idx] == ".":
            output = output + "."
        else:
            output = output + "#"
    return output

# First double up any blank rows and columns

doubled_rows = []

clear_cols_map = "." * len(input_image[0])

for line in input_image:
    clear_cols_map = xor_strings(clear_cols_map,line)
    if line.find("#") == -1:
        # No galaxies in this line, so double up
        doubled_rows.append(line.strip())
    doubled_rows.append(line.strip())

final_expansion_image = []

for line in doubled_rows:
    expanded_line = []
    for idx, char in enumerate(line): 
        if clear_cols_map[idx] == ".":
            expanded_line.append(char)
        expanded_line.append(char)

    final_expansion_image.append(expanded_line)

# Next establish a list of galaxies

galaxies = []
galaxy_id = 0

for ridx, row in enumerate(final_expansion_image):
    for cidx, char in enumerate(row):
        if char == "#":
            galaxies.append({"id":galaxy_id,"row":ridx,"col":cidx})
            galaxy_id += 1


# Next compute the distances between each pair:
sum_distances = 0

for start_galaxy in galaxies:
    for end_galaxy in galaxies:
        sum_distances += abs(end_galaxy["row"]-start_galaxy["row"]) + abs(end_galaxy["col"]-start_galaxy["col"])

sum_distances = int(sum_distances / 2)

# Can ignore the case of computing distance to self as it's 0 anyway
# Can also just divide by two as we've computed every pair twice; easier than keeping track...

print("The sum of the distances between galaxies is: " + str(sum_distances))