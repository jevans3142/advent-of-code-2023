import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

card_total = 0

winning_cards_record = []

for line in f:
    card = int(line[4 : line.index(":")])

    winning_numbers = line[line.index(":") + 1 : line.index("|")].split()

    possible_numbers = line[line.index("|") + 1 :].split()

    this_card_matching_numbers = 0
    for test_num in winning_numbers:
        if test_num in possible_numbers:
            this_card_matching_numbers = this_card_matching_numbers + 1

    winning_cards_record.append([card, 1, this_card_matching_numbers])

for card in winning_cards_record:
    print(card)
    card_total = card_total + card[1]
    for idx in range(card[0], card[0] + card[2]):
        print(idx)
        winning_cards_record[idx][1] += card[1]

print("The total number of cards is: " + str(card_total))
