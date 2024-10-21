# This class have a card list. It will appened the suits to each card, return a deck, shuffles a deck, and distribute cards

from Card import Card
import random
class Deck:
    def __init__(self):
        self.cards=[Card(suit, rank) for rank in range(2, 15) for suit in ("clubs", "diamonds", "spades", "hearts")]

    def get_deck(self):
        return self.cards
    
    def print_deck(self):  
        print(*self.cards,sep='\n') 

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            print("Deck is empty.")
            return None

        
if __name__ == '__main__':
    card1 = Deck()
    print(card1.get_deck())
    card1.print_deck()