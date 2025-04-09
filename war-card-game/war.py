import random
import time

deck = []
rank = 2

def append_rank(card_rank):
    deck.append([card_rank, rank])

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

while True:
    shuffled_deck = deck.copy()
    random.shuffle(shuffled_deck)

    p1_deck = shuffled_deck[26:]
    p2_deck = shuffled_deck[:26]

    p1_card, p1_rank = p1_deck[0][0], p1_deck[0][1]
    p2_card, p2_rank = p2_deck[0][0], p2_deck[0][1]
    print(f"P1: {p1_card} {p1_rank}...")
    print(f"P2: {p2_card} {p2_rank}...")
    if p1_rank > p2_rank:
        print("P1 Wins!")
    elif p1_rank == p2_rank:
        print("It's war time!")
    else:
        print("P2 Wins!")
    time.sleep(2)
