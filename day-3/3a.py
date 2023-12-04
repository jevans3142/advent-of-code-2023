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

parts_total = 0


def char_is_valid_symbol(char):
    if char == ".":
        return False
    if char.isdigit():
        return False
    if char.isalnum():
        return False
    return True


# First add dots surrounding the whole file to handle going off the start/ends of the lines - total hack but whatever
process_data_temp = []
for line in f: # test
    process_data_temp.append(line)
process_data = []

line_length = len(process_data_temp[0])
process_data_temp.insert(0, ("." * line_length))
process_data_temp.append(("." * line_length))
for line in process_data_temp:
    process_data.append("." + line[:-1] + ".") # have to add the -1 to chop the newline off the end....

print(process_data)

# Now we've rendered the edges safe....

for lnidx, line in enumerate(process_data):
    current_num = ""
    for charidx, char in enumerate(line):
        # Scan through looking for numbers using a simple state machine
        if char.isdigit():
            current_num = current_num + str(char)
            continue
        if current_num != "":
            # Then we've got to the end of a number, and need to work out if it's a valid part number
            # so check if there's a symbol - need to be careful to handle wrapping at start/end etc
            symbol_seen = False
            # Character before
            if char_is_valid_symbol(line[charidx - len(current_num) - 1]):
                symbol_seen = True
            # Character after (which is the one we're currently on anyway)
            if char_is_valid_symbol(char):
                symbol_seen = True

            # Line before
            for test_char in process_data[lnidx - 1][
                charidx - len(current_num) - 1 : charidx + 1
            ]:
                if char_is_valid_symbol(test_char):
                    symbol_seen = True

            # Line after
            for test_char in process_data[lnidx + 1][
                charidx - len(current_num) - 1 : charidx + 1
            ]:
                if char_is_valid_symbol(test_char):
                    symbol_seen = True

            print(
                process_data[lnidx - 1][charidx - len(current_num) - 1 : charidx + 1]
                + "\n"
                + line[charidx - len(current_num) - 1] + str(current_num) + char 
                + "\n"
                + process_data[lnidx + 1][charidx - len(current_num) - 1 : charidx + 1]
            )

            if symbol_seen == True:
                print("YES")
                parts_total = parts_total + int(current_num)
            current_num = ""
            print()

print("The sum of the part numbers is: " + str(parts_total))