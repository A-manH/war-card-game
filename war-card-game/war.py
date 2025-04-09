import random
import time
import msg

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

shuffled_deck = deck.copy()
random.shuffle(shuffled_deck)

p1_deck = shuffled_deck[26:]
p2_deck = shuffled_deck[:26]

while True:
    p1_card, p1_rank = p1_deck[0][0], p1_deck[0][1]
    p2_card, p2_rank = p2_deck[0][0], p2_deck[0][1]

    print(f"P1: {p1_card} {p1_rank}...")
    print(f"P2: {p2_card} {p2_rank}...")
    if p1_rank > p2_rank:
        winner_card = p1_deck.pop(0)
        p1_deck.append(winner_card)

        loser_card = p2_deck.pop(-1)
        p1_deck.append(loser_card)

        print("P1 won the trade")
        print(f"P1: {len(p1_deck)} cards | P2: {len(p2_deck)} cards\n")
    # elif p1_rank == p2_rank:
    #     msg.slowprint("I... Delare... War!\n")

    #     print(f"P1: {len(p1_deck)} cards | P2: {len(p2_deck)} cards\n")
    else:
        winner_card = p2_deck.pop(0)
        p2_deck.append(winner_card)

        loser_card = p1_deck.pop(-1)
        p2_deck.append(loser_card)

        print("P2 won the trade")
        print(f"P1: {len(p1_deck)} cards | P2: {len(p2_deck)} cards\n")
    # time.sleep(.03)

    if len(p1_deck) == 0:
        msg.slowprint("P2 wins by a land slide. You suck P1!")
        break
    if len(p2_deck) == 0:
        msg.slowprint("You can do better than that, P1. P2 wins *sigh")
        break