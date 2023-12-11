import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

input_image = f.readlines()


def xor_strings(input1, input2):
    output = ""
    for idx, char in enumerate(input1):
        if input1[idx] == "." and input2[idx] == ".":
            output = output + "."
        else:
            output = output + "#"
    return output


# First establish a list of galaxies

galaxies = []
galaxy_id = 0

for ridx, row in enumerate(input_image):
    for cidx, char in enumerate(row):
        if char == "#":
            galaxies.append({"id": galaxy_id, "row": ridx, "col": cidx})
            galaxy_id += 1

# Now establish a map of rows and columns that are clear and will expand

rows_to_expand = []
cols_to_expand = []

clear_cols_map = "." * len(input_image[0])

for ridx, row in enumerate(input_image):
    clear_cols_map = xor_strings(clear_cols_map, row)
    if row.find("#") == -1:
        rows_to_expand.append(ridx)

for cidx, char in enumerate(clear_cols_map):
    if char == ".":
        cols_to_expand.append(cidx)

print(rows_to_expand)
print(cols_to_expand)

# Finally compute the distances between each pair:
sum_distances = 0

for start_galaxy in galaxies:
    for end_galaxy in galaxies:
        start_row = start_galaxy["row"] + 999999 * len(
            list(filter(lambda x: x < start_galaxy["row"], rows_to_expand))
        )
        end_row = end_galaxy["row"] + 999999 * len(
            list(filter(lambda x: x < end_galaxy["row"], rows_to_expand))
        )

        start_col = start_galaxy["col"] + 999999 * len(
            list(filter(lambda x: x < start_galaxy["col"], cols_to_expand))
        )
        end_col = end_galaxy["col"] + 999999 * len(
            list(filter(lambda x: x < end_galaxy["col"], cols_to_expand))
        )

        sum_distances += abs(end_row - start_row) + abs(end_col - start_col)

sum_distances = int(sum_distances / 2)

# Can ignore the case of computing distance to self as it's 0 anyway
# Can also just divide by two as we've computed every pair twice; easier than keeping track...

print("The sum of the distances between galaxies is: " + str(sum_distances))
