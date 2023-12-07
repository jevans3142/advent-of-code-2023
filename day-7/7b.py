import os
import math

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high_card = []

card_values = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}


def hand_value(hand):
    value = (
        int(card_values.get(hand[0], hand[0])) * int(math.pow(14, 4))
        + int(card_values.get(hand[1], hand[1])) * int(math.pow(14, 3))
        + int(card_values.get(hand[2], hand[2])) * int(math.pow(14, 2))
        + int(card_values.get(hand[3], hand[3])) * int(math.pow(14, 1))
        + int(card_values.get(hand[4], hand[4])) * int(math.pow(14, 0))
    )
    return value


def decompose_hand(hand):
    decomposition = {}
    for x in hand:
        decomposition[x] = decomposition.get(x, 0) + 1
    return decomposition


# First load in the hands into the correct types
for line in f:
    hand = line.split()[0]
    bid = int(line.split()[1])

    decomp = decompose_hand(hand)
    
    # Now we 'upgrade' the decomp if there are any jokers
    if decomp.get("J", None ) != None:
        # There are some jokers
        joker_number = decomp["J"]
        no_jokers = decomp.pop("J")
        # Get the largest remaining set of cards and add the jokers to it 
        decomp_values = list(sorted(decomp.values()))
        # Handle the all joker case... 
        if decomp_values == []:
            decomp_values = [0]
        decomp_values[-1] += joker_number
    else:
        # No jokers
        decomp_values = list(sorted(decomp.values()))

    # First check if it's five of a kind
    if decomp_values == [5]:
        five_kind.append({"hand": hand, "bid": bid})
        continue

    # Four of a kind
    if decomp_values == [1, 4]:
        four_kind.append({"hand": hand, "bid": bid})
        continue

    # Full house
    if decomp_values == [2, 3]:
        full_house.append({"hand": hand, "bid": bid})
        continue

    # Three of a kind
    if decomp_values == [1, 1, 3]:
        three_kind.append({"hand": hand, "bid": bid})
        continue

    # Two pair
    if decomp_values == [1, 2, 2]:
        two_pair.append({"hand": hand, "bid": bid})
        continue

    # One pair
    if decomp_values == [1, 1, 1, 2]:
        one_pair.append({"hand": hand, "bid": bid})
        continue

    # Must therefore be high card
    high_card.append({"hand": hand, "bid": bid})

five_kind.sort(key=lambda x: hand_value(x["hand"]), reverse=True)
four_kind.sort(key=lambda x: hand_value(x["hand"]), reverse=True)
full_house.sort(key=lambda x: hand_value(x["hand"]), reverse=True)
three_kind.sort(key=lambda x: hand_value(x["hand"]), reverse=True)
two_pair.sort(key=lambda x: hand_value(x["hand"]), reverse=True)
one_pair.sort(key=lambda x: hand_value(x["hand"]), reverse=True)
high_card.sort(key=lambda x: hand_value(x["hand"]), reverse=True)

complete_list = (
    five_kind + four_kind + full_house + three_kind + two_pair + one_pair + high_card
)
top_rank = len(complete_list)

total_winnings = 0
for hand in complete_list:
    total_winnings = total_winnings + hand["bid"] * top_rank
    top_rank -= 1

print("The total winnings are:" + str(total_winnings))
