from math import e
import random
import time
import msg

class PlayerDeck:
    def __init__(self, deck, name):
        self.deck = deck
        self.name = name

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

player_1 = PlayerDeck(shuffled_deck[26:], "P1")
player_2 = PlayerDeck(shuffled_deck[26:], "P2")
p1_deck = player_1.deck
p2_deck = player_2.deck

while True:
    p1_card, p1_rank = p1_deck[0][0], p1_deck[0][1]
    p2_card, p2_rank = p2_deck[0][0], p2_deck[0][1]
    P1_WIN_TRADE = p1_rank > p2_rank
    P2_WIN_TRADE = p2_rank > p1_rank
    I_DECLARE_WAR = p1_rank == p2_rank

    print(f"P1: played {p1_card}...")
    print(f"P2: played {p2_card}...")
    if P1_WIN_TRADE:
        winner_card = p1_deck.pop(0)
        p1_deck.append(winner_card)

        loser_card = p2_deck.pop(-1)
        p1_deck.append(loser_card)

        print("P1 won the trade")
        print(f"P1: {len(p1_deck)} cards | P2: {len(p2_deck)} cards\n")
    elif P2_WIN_TRADE:
        winner_card = p2_deck.pop(0)
        p2_deck.append(winner_card)

        loser_card = p1_deck.pop(-1)
        p2_deck.append(loser_card)

        print("P2 won the trade")
        print(f"P1: {len(p1_deck)} cards | P2: {len(p2_deck)} cards\n")
    elif I_DECLARE_WAR:
        msg.slowprint("I... Declare... War!\n", space_speed=0.53)

        p1_wardeck = p1_deck[:4]        
        p2_wardeck = p2_deck[:4]
        for player in (player_1, player_2):
            print(f"{player.name} got: ")
            for card in p1_wardeck:
                msg.slowprint(card[-1], end=", ")
        time.sleep(5)

        print(f"P1: {len(p1_deck)} cards | P2: {len(p2_deck)} cards\n")
    time.sleep(2.5)

    if len(p1_deck) == 0:
        msg.slowprint("P2 wins by a land slide. You suck P1!", space_speed=0)
        break
    if len(p2_deck) == 0:
        msg.slowprint("You can do better than that, P1. P2 wins *sigh")
        break