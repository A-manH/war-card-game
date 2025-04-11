import random
import time
import msg
from classes import Deck, Player

deck = Deck.new_deck()
print(deck)
shuffled_deck = Deck.shuffle(deck)

player_1 = Player(shuffled_deck[:26], "P1")
player_2 = Player(shuffled_deck[26:], "P2")
p1_deck = player_1.deck
p2_deck = player_2.deck

while True:
    p1_card, p1_rank = p1_deck[0][0], p1_deck[0][1]
    p2_card, p2_rank = p2_deck[0][0], p2_deck[0][1]
    player_1.wardeck = p1_deck[:4]
    player_2.wardeck = p2_deck[:4]
    p1_war_rank = player_1.wardeck[0][1]
    p2_war_rank = player_2.wardeck[0][1]
    P1_WIN_TRADE = p1_rank > p2_rank
    P2_WIN_TRADE = p2_rank > p1_rank
    I_DECLARE_WAR = p1_rank == p2_rank
    round_pause = time.sleep

    print(f"P1: played {p1_card}...")
    print(f"P2: played {p2_card}...")
    if P1_WIN_TRADE:
        winner_card = p1_deck.pop(0)
        p1_deck.append(winner_card)

        loser_card = p2_deck.pop()
        p1_deck.append(loser_card)

        print("P1 won the trade")
        print(f"P1: {len(p1_deck)} cards | P2: {len(p2_deck)} cards\n")

    elif P2_WIN_TRADE:
        winner_card = p2_deck.pop(0)
        p2_deck.append(winner_card)

        loser_card = p1_deck.pop()
        p2_deck.append(loser_card)

        print("P2 won the trade")
        print(f"P1: {len(p1_deck)} cards | P2: {len(p2_deck)} cards\n")

    elif I_DECLARE_WAR:
        msg.slowprint("I... Declare... War!\n", space_speed=0.53)

        for player in (player_1, player_2):
            print(f"{player.name} got: ", end="")
            for card in player.wardeck:
                print(card[0], end=", ")

        if p1_war_rank > p2_war_rank:
            player_1.deck.extend(player_2.wardeck)
            del player_2.deck[:4]
            print("P1 won the war")

        elif p2_war_rank > p1_war_rank:
            player_2.deck.extend(player_1.wardeck)
            del player_1.deck[:4]
            print("P2 won the war")
        elif p1_war_rank == p2_war_rank:
            print("Its a tie again!")

        # print(f"P1{player_1.deck} \nP2{player_2.deck}\n\n")
        # print(f"P1{player_1.wardeck} \nP2{player_2.wardeck}")

        print(f"P1: {len(p1_deck)} cards | P2: {len(p2_deck)} cards\n")
        time.sleep(5)

    round_pause(2)

    if len(p1_deck) == 0:
        msg.slowprint("P2 wins by a land slide. You suck P1!", space_speed=0)
        break
    if len(p2_deck) == 0:
        msg.slowprint("You can do better than that, P1. P2 wins *sigh")
        break