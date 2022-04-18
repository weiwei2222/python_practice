logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


bids = {"Make": 234, "Lily": 345, "Mike": 8856}


def find_highest_bidder(find_bidder):
    highest_bid = 0
    winner = ""
    for bidders in find_bidder:
        bid_amount = find_bidder[bidders]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidders
    print(f"The winner is {winner} with a bid of ${highest_bid}")


find_highest_bidder(bids)
