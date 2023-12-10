import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

def make_difference_list(input_list):
    new_list = []
    for idx in range(0, len(input_list)-1):
        new_list.append(input_list[idx+1]-input_list[idx])
    if new_list.count("0")==len(new_list):
        # All zeros - so now we need to work our way back up
        return input_list[-1]
    else: 
        # Not yet all zeros - so recurse into next level
        return input_list[-1] + make_difference_list(new_list)
    
sum = 0

for history in f:
    # Loop though each line
    numbers = list(map(lambda x: int(x), history.split()))
    
    next_value = make_difference_list(numbers)
    sum += next_value

print("The sum of the values is:" + str(sum))
