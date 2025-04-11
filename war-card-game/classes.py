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
    
    def add_card(self):
        pass

    def remove_card(self):
        pass
    
    def deck_length(self):
        pass