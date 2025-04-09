import random

deck = {}
rank = 2

def append_rank(card_rank):
    if str(rank) in deck:
        deck[str(rank)].append(card_rank)
    else:
        deck.update({str(rank): [card_rank]})

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

shuffled_deck = list(deck)
random.shuffle(shuffled_deck)
print(dict((shuffled_deck)))

