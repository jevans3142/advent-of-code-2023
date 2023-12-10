import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

all_lines = f.readlines()

# First get the direction string
direction_string = all_lines[0]
all_lines.pop(0)
all_lines.pop(0)  # Account for the blank line

direction_string = direction_string.rstrip()

# Now load in the nodes
nodes = {}
for line in all_lines:
    node_name = line[0:3]
    node_left = line[7:10]
    node_right = line[12:15]
    nodes[node_name] = [node_left, node_right]
    
current_node = "AAA"
steps_taken = 0
direction_index = 0
while True:
    if direction_index >= len(direction_string):
        direction_index = 0

    if direction_string[direction_index] == "L":
        current_node = nodes[current_node][0]
    if direction_string[direction_index] == "R":
        current_node = nodes[current_node][1]

    if current_node=="ZZZ":
        steps_taken += 1
        break
    else:
        steps_taken += 1
        direction_index += 1


print("Steps taken to reach ZZZ:" + str(steps_taken))
