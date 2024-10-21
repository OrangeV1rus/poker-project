# Hand class have a hand list. It add cards into the hand list, and can rank the hand. If the rank of two hands are the same, there will be a compare method wihch will compare the 
# two hands and return who wins or still a tie. 

from Card import Card
class Hand:
    def __init__(self):
        self.hand = []
    
    def get_hand(self):
        return self.hand
    
    def print_hand(self):
        print(*self.hand,sep='\n') 
    
    def add_card(self, card):
        self.hand.append(card)
        self.hand.sort(key = Card.get_value, reverse=True)
    
    def rank(self):
        if self.is_royal_flush():
            return 9
        elif self.is_straight_flush():
            return 8
        elif self.is_four_of_a_kind():
            return 7
        elif self.is_full_house():
            return 6
        elif self.is_flush():
            return 5
        elif self.is_straight():
            return 4
        elif self.is_three_of_a_kind():
            return 3
        elif self.is_two_pair():
            return 2
        elif self.is_one_pair():
            return 1
        else:
            return 0


    def is_royal_flush(self):
        is_royal_flush = False
        if self.is_straight_flush() == True and self.hand[0].get_value() == 14:
                is_royal_flush = True
        return is_royal_flush
        

    def is_straight_flush(self):
        is_full_house = False
        if self.is_straight() == True and self.is_flush() == True:
            is_full_house = True
        return is_full_house        

    def is_four_of_a_kind(self):
        is_four_of_a_kind = False
        count = 0
        for i in range(len(self.hand)-3):
            if self.hand[i].get_value() == self.hand[i+1].get_value() == self.hand[i+2].get_value() == self.hand[i+3].get_value():
                count += 1
        if count == 1:
            is_four_of_a_kind = True
        return is_four_of_a_kind            

    def is_full_house(self):
        is_full_house = False
        if self.is_twos_pair():
            if self.is_three_of_a_kind():
                is_full_house = True
        return is_full_house 
        
    def is_flush(self):
        is_flush = False
        count = 0
        for i in range(len(self.hand)-1):
            if self.hand[i].get_suit() == self.hand[i+1].get_suit():
                count += 1
        if count == 4:
            is_flush = True
        return is_flush

        
    def is_straight(self):
        is_straight = False
        count = 0
        for i in range(len(self.hand)-1):
            if self.hand[i].get_value()- self.hand[i+1].get_value() == 1:
                count += 1
        if count == 4:
            is_straight = True
        return is_straight

        
    def is_three_of_a_kind(self):
        is_three_of_a_kind = False
        count = 0
        for i in range(len(self.hand)-2):
            if self.hand[i].get_value() == self.hand[i+1].get_value() == self.hand[i+2].get_value():
                count += 1
        if count == 1:
            is_three_of_a_kind = True
        return is_three_of_a_kind

    def is_twos_pair(self):
        is_two_pair = False
        count = 0
        for i in range(len(self.hand)-1):
            if self.hand[i].get_value() == self.hand[i+1].get_value():
                count += 1
        if count == 3:
            is_two_pair = True
        return is_two_pair 
    
    def is_two_pair(self):
        is_two_pair = False
        count = 0
        for i in range(len(self.hand)-1):
            if self.hand[i].get_value() == self.hand[i+1].get_value():
                count += 1
        if count == 2:
            is_two_pair = True
        return is_two_pair       

    def is_one_pair(self):
        is_one_pair = False
        count = 0
        for i in range(len(self.hand)-1):
            if self.hand[i].get_value() == self.hand[i+1].get_value():
                count += 1
        if count == 1:
            is_one_pair = True
        return is_one_pair

    def get_hand_type(self):
        if self.rank() == 0:
            return("High Card")
        elif self.rank() == 1:
            return("One Pair")
        elif self.rank() == 2:
            return("Two Pair")
        elif self.rank() == 3:
            return("Three-of-a-kind")
        elif self.rank() == 4:
            return("Straight")
        elif self.rank() == 5:
            return("Flush")
        elif self.rank() == 6:
            return("Full House")
        elif self.rank() == 7:
            return("Four-of-a-kind")
        elif self.rank() == 8:
            return("Straight Flush")
        elif self.rank() == 9:
            return("Royal Flush")
    
    def compare(self, other_hand):
        if other_hand.rank() > self.rank():
            return -1
        elif self.rank() > other_hand.rank():
            return 1
        else:
            if self.rank() == 9:  # Royal Flush
                return 0 
            elif self.rank() == 8:  # Straight Flush
                return self.compare_highest_card(other_hand)

            elif self.rank() == 7:  # Four-of-a-kind
                return self.compare_four_of_a_kind(other_hand)

            elif self.rank() == 6:  # Full House
                return self.compare_full_house(other_hand)

            elif self.rank() == 5:  # Flush
                return self.compare_highest_card(other_hand)

            elif self.rank() == 4:  # Straight
                return self.compare_highest_card(other_hand)

            elif self.rank() == 3:  # Three-of-a-kind
                return self.compare_three_of_a_kind(other_hand)

            elif self.rank() == 2:  # Two Pair
                return self.compare_two_pair(other_hand)

            elif self.rank() == 1:  # One Pair
                return self.compare_one_pair(other_hand)
            
            elif self.rank() == 0: 
                return self.compare_highest_card(other_hand)
            
    def compare_highest_card(self, other_hand):
        if self.hand[0].get_value() > other_hand.hand[0].get_value():
            return 1
        elif self.hand[0].get_value() < other_hand.hand[0].get_value():
            return -1
        else:
            return 0
        
    def compare_one_pair(self, other_hand):
        for i in range(len(self.hand)-1):
            if self.hand[i].get_value() == self.hand[i+1].get_value():
                for j in range(len(other_hand.hand)-1):
                    if other_hand.hand[j].get_value() == other_hand.hand[j+1].get_value():
                        if other_hand.hand[j].get_value() < self.hand[i].get_value():
                            return 1
                        elif other_hand.hand[j].get_value() > self.hand[i].get_value():
                            return -1
                        elif other_hand.hand[j].get_value() == self.hand[i].get_value():
                            if other_hand.hand[0].get_value() > self.hand[0].get_value():
                                return -1
                            elif other_hand.hand[0].get_value() < self.hand[0].get_value():
                                return 1
                            else:
                                return 0 
                            
    def compare_three_of_a_kind(self, other_hand):
        if self.hand[2].get_value() > other_hand.hand[2].get_value():
            return 1
        elif self.hand[2].get_value() < other_hand.hand[2].get_value():
            return -1
        else:
            return 0
        
    def compare_full_house(self,other_hand):
        if self.hand[2].get_value() > other_hand.hand[2].get_value():
            return 1
        elif self.hand[2].get_value() < other_hand.hand[2].get_value():
            return -1
        else:
            return 0
        
    def compare_four_of_a_kind(self,other_hand):
        if self.hand[2].get_value() > other_hand.hand[2].get_value():
            return 1
        elif self.hand[2].get_value() < other_hand.hand[2].get_value():
            return -1
        else:
            return 0
                
    def compare_two_pair(self, other_hand):
        for i in range(len(self.hand)-1):
            if self.hand[i].get_value() == self.hand[i+1].get_value():
                for j in range(len(other_hand.hand)-1):
                    if other_hand.hand[j].get_value() == other_hand.hand[j+1].get_value():
                        if other_hand.hand[j].get_value() < self.hand[i].get_value():
                            return 1
                        elif other_hand.hand[j].get_value() > self.hand[i].get_value():
                            return -1
                        elif other_hand.hand[j].get_value() == self.hand[i].get_value():
                           for y in range(len(self.hand)-1): 
                                if self.hand[y+i+2].get_value() == self.hand[y+i+3].get_value():
                                    for x in range(len(other_hand.hand)-1): 
                                        if other_hand.hand[x+j+2].get_value() == other_hand.hand[x+j+3].get_value():
                                            if other_hand.hand[x+j+2].get_value() > self.hand[y+i+2].get_value():
                                                return -1
                                            elif other_hand.hand[x+j+2].get_value() < self.hand[y+i+2].get_value():
                                                return 1
                                            elif other_hand.hand[x+j+2].get_value() == self.hand[y+i+2].get_value():
                                                if other_hand.hand[0].get_value() > self.hand[0].get_value():
                                                    return -1
                                                elif other_hand.hand[0].get_value() < self.hand[0].get_value():
                                                    return 1
                                                else:
                                                    return 0                 


if __name__ == '__main__':

    hand1 = Hand()
    hand2 = Hand()

    card1 = Card("Hearts", 10)
    card2 = Card("Hearts", 10)
    card3 = Card("Hearts", 10)
    card4 = Card("Hearts", 9)
    card5 = Card("Heart", 9)

    card6 = Card("hessarts", 2)
    card7 = Card("hessarts", 3)
    card8 = Card("hessarts", 4)
    card9 = Card("hessarts", 5)
    card10 = Card("hessarts", 6)

    hand1.add_card(card1)
    hand1.add_card(card2)
    hand1.add_card(card3)
    hand1.add_card(card4)
    hand1.add_card(card5)

    hand2.add_card(card6)
    hand2.add_card(card7)
    hand2.add_card(card8)
    hand2.add_card(card9)
    hand2.add_card(card10)

    print(hand1.get_hand_type())
    print(hand1.is_full_house())
    print(hand1.is_one_pair())
    print(hand1.is_three_of_a_kind())