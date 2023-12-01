input_file = "input.txt"

sum = 0

f = open(input_file, "r")

test = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

for line in f:
    first_digit = ""
    last_digit = ""

    for idx, char in enumerate(line):
        if char.isdigit():
            if first_digit == "":  # ie. we haven't seen either digit yet
                first_digit = str(char)
                last_digit = str(char)
            else:  # ie. we have seen the first digit
                last_digit = str(char)
        else: # it's not a numeric digit - so assume it's text
            for idx2, digit in enumerate(digits): # heavily inefficient this but who cares
                if line[idx:].startswith(digit): 
                    if first_digit == "":  # ie. we haven't seen either digit yet
                        first_digit = str(idx2 + 1)
                        last_digit = str(idx2 + 1)
                    else:  # ie. we have seen the first digit
                        last_digit = str(idx2 + 1)
                    continue

                    
    if first_digit == "":  # Handles the edge case with no digits at all
        continue

    this_line = int(str(first_digit + last_digit))
    print(this_line)
    sum = sum + this_line


print("The total value is: " + str(sum))
