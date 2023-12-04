import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

points_total = 0

for line in f:
    card = int(line[4 : line.index(":")])

    winning_numbers = line[line.index(":")+1 : line.index("|")].split()

    possible_numbers = line[line.index("|")+1:].split()

    this_card_points = 0 
    for test_num in winning_numbers:
        if test_num in possible_numbers:
            if this_card_points == 0:
                this_card_points = 1
            else:
                this_card_points = this_card_points * 2

    points_total = points_total + this_card_points

print("The sum of the points is: " + str(points_total))
