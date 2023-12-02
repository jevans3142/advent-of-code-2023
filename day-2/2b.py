import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

power_total = 0

for line in f:
    id = int(line[5 : line.index(":")])

    cubes_max_this_game = {"red": 0, "green": 0, "blue": 0}

    sub_games = line[line.index(":") + 1 :].split(";")

    for sub_game in sub_games:
        each_colour = sub_game.split(",")
        for colour in each_colour:
            components = colour.split()
            if int(components[0]) > cubes_max_this_game[components[1]]:
                # Then we need to increase the max number of this colour of cube
                cubes_max_this_game[components[1]] = int(components[0]) 

    power_total = power_total + (
        cubes_max_this_game["blue"]
        * cubes_max_this_game["red"]
        * cubes_max_this_game["green"]
    )

print("The sum of the powers is: " + str(power_total))
