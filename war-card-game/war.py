import random

deck = []
print(deck)
rank = 2

def append_rank(card_rank):
    deck.append({card_rank: rank})

for ranks in range(13):
    for card in range(4):
        if rank == 11:
            append_rank("Jack")
        elif rank == 12:
            append_rank("Queen")
        elif rank == 13:
            append_rank("King")
        elif rank == 14:
            append_rank("Ace")
        else:
            append_rank(rank)
    rank += 1
print(deck)
# shuffled_deck = list(deck.items())
# random.shuffle(shuffled_deck)
# print(shuffled_deck[:6])
# print(shuffled_deck[6:])