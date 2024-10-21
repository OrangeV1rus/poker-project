# The attribute is suit and value, this class card is generating the image file name, name of the card, value, and suit. 

import csv
class Card:
    def __init__(self, suit: str, value: int):
        self.suit=suit
        self.value=value

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit
    
    def __repr__(self):
        
        special_names = {2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",11:"Jack",12:"Queen",13:"King",14:"Ace"}
 
        name = special_names.get(self.value, str(self.value))

        return f"{name} of {self.suit}"


    def image_file_name(self):
        specials_names = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10",11:"jack",12:"queen",13:"king",14:"ace"}
        names = specials_names.get(self.value, str(self.value))
        
        return f"C:/Users/jacob/REXSHISHABI/Poker project/pictures/{names}_of_{self.suit}.png"
    
   
if __name__ == '__main__':
    card1 = Card("hearts", 3)
    print(card1.__repr__())
    print(card1.image_file_name())