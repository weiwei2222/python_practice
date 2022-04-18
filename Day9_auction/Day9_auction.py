from replit import clear
from Day9_art import logo
print(logo)

bids = {}
bid_finished = False


def find_highest_bidder(biding_record):
    highest_bid = 0
    winner = ""
    for bidder in biding_record:
        bid_amount = biding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bid_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidder?Type 'yes' or 'no'!\n")
    if should_continue == "no":
        bid_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

