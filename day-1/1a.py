

input_file = "input.txt"

sum = 0 

f = open(input_file,"r")

test = ["1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet", "hello"]

for line in f:
    first_digit = ""
    last_digit = ""

    for char in line:
        if char.isdigit():
            if first_digit == "": # ie. we haven't seen either digit yet  
                first_digit = str(char)
                last_digit = str(char)
            else: # ie. we have seen the first digit
                last_digit = str(char)

    if (first_digit==""): # Handles the edge case with no digits at all 
        continue

    this_line = int(str(first_digit + last_digit))
    print(this_line)
    sum = sum + this_line


print("The total value is: " + str(sum))