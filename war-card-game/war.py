import random
from tracemalloc import start

deck = []
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

shuffled_deck = deck.copy()
random.shuffle(shuffled_deck)

player1 = [shuffled_deck[26:]]
player2 = [shuffled_deck[:26]]
players = (player1, player2)
starting_player = players[random.randint(0, 1)]
print(starting_player)
