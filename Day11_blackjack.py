import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    get_card = random.choice(cards)
    return get_card


user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(get_card):
    if sum(get_card) == 21 and len(get_card) == 2:
        return 0
    if 11 in get_card and sum(get_card) > 2:
        get_card.remove(11)
        get_card.append(1)
    return sum(get_card)

