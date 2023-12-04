import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

test = [
    "467..114..\n",
    "...*......\n",
    "..35..633.\n",
    "......#...\n",
    "617*......\n",
    ".....+.58.\n",
    "..592.....\n",
    "......755.\n",
    "...$.*....\n",
    ".664.598..\n",
]

ratio_total = 0

# First add dots surrounding the whole file to handle going off the start/ends of the lines - total hack but whatever
process_data_temp = []
gear_map = [] 
for line in f:  # test
    process_data_temp.append(line)
    
process_data = []

line_length = len(process_data_temp[0])
process_data_temp.insert(0, ("." * line_length))
process_data_temp.append(("." * line_length))
for line in process_data_temp:
    process_data.append(
        "." + line[:-1] + "."
    )  # have to add the -1 to chop the newline off the end....
    gear_map.append( "." + "." * len(line[:-1]) + ".")

# Now we've rendered the edges safe....

for lnidx, line in enumerate(process_data):
    current_num = ""
    for charidx, char in enumerate(line):
        # Scan through looking for numbers using a simple state machine
        if char.isdigit():
            current_num = current_num + str(char)
            continue
        if current_num != "":
            # Then we've got to the end of a number, and need to work out if it's part of a gear...
            gear_seen = False
            gear_coords = [0,0]
            # Character before
            if line[charidx - len(current_num) - 1] == "*":
                gear_seen = True
                gear_coords = [lnidx,charidx - len(current_num) - 1]

            # Character after (which is the one we're currently on anyway)
            if char == "*":
                gear_seen = True
                gear_coords = [lnidx,charidx]

            # Line before
            for scanidx, test_char in enumerate(process_data[lnidx - 1][
                charidx - len(current_num) - 1 : charidx + 1
            ]):
                if test_char == "*":
                    gear_seen = True
                    gear_coords = [lnidx-1,charidx - len(current_num) - 1 + scanidx]

            # Line after
            for test_char in process_data[lnidx + 1][
                charidx - len(current_num) - 1 : charidx + 1
            ]:
                if test_char == "*":
                    gear_seen = True
                    gear_coords = [lnidx+1,charidx - len(current_num) - 1 + scanidx]

            if gear_seen == True:

                # Is this the first or the second time we've seen this gear? 

                if(gear_map[gear_coords[0], gear_coords[1]]=="."):
                    # First time

                parts_total = parts_total + int(current_num)
            current_num = ""

print("The sum of the gear ratios is: " + str(ratio_total))
