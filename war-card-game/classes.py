import random
class Deck:
    def new_deck():
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
        return deck
    def shuffle(deck):
        shuffled_deck = deck.copy()
        random.shuffle(shuffled_deck)
        return shuffled_deck

class Player:
    def __init__(self, deck, name, wardeck=None):
        self.deck = deck
        self.name = name
        self.wardeck = wardeck
    
    def steal_card(self, loser):
        winner_card = self.pop(0)
        self.append(winner_card)

        loser_card = loser.pop()
        self.append(loser_card)
    
    def steal_hand(self, loser):
        loser_hand = loser.deck[-4:]
        del loser.deck[-4:]
        self.deck.append(loser_hand)


    def deck_length(self):
        return len(self.deck)