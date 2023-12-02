import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

cubes_max = {"red": 12, "green": 13, "blue": 14}

id_total = 0

for line in f:
    id = int(line[5 : line.index(":")])

    game_possible_flag = True

    sub_games = line[line.index(":") + 1 :].split(";")

    for sub_game in sub_games:
        each_colour = sub_game.split(",")
        for colour in each_colour:
            components = colour.split()
            if int(components[0]) > cubes_max[components[1]]:
                # Then this sub game was not possible, and therefore neither was this game
                game_possible_flag = False

    if game_possible_flag == True:
        id_total = id_total + id

print("The sum of the ids of the possible games is: " + str(id_total))
