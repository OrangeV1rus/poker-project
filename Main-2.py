# The main scipt have images and hands attributes. It takes images of cards from a folder and display it in rows. the picture displayed 
# will have 4 player's hand and what rank they have. It will also compare the hands and tell who wins. 


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from Deck import Deck
from Hand import Hand

def make_row(im1, im2, im3, im4, im5):
    row = Image.new('RGB', (im1.width * 6, im1.height))
    row.paste(im1, (0, 0))
    row.paste(im2, (im1.width, 0))
    row.paste(im3, (im1.width *2, 0))
    row.paste(im4, (im1.width *3, 0))
    row.paste(im5, (im1.width *4, 0))
    return row

def makegrid(im1, im2, im3, im4):
    row = Image.new('RGB', (im1.width, im1.height * 4))
    row.paste(im1, (0, 0))
    row.paste(im2, (0, im1.height))
    row.paste(im3, (0, im1.height *2))
    row.paste(im4, (0, im1.height* 3))
    return row



hand1=Hand()
hand2=Hand()
hand3=Hand()
hand4=Hand()

deck = Deck()
deck.shuffle()

for x in range(5):
    hand1.add_card(deck.deal_card())
    hand2.add_card(deck.deal_card())
    hand3.add_card(deck.deal_card())
    hand4.add_card(deck.deal_card())

poker_game=[]
poker_game.append(hand1)
poker_game.append(hand2)
poker_game.append(hand3)
poker_game.append(hand4)

def comparefour():
    if hand1.compare(hand2) == 1 and hand1.compare(hand3) == 1 and hand1.compare(hand4) == 1:
        return 85
    elif hand2.compare(hand1) ==1 and hand2.compare(hand3) == 1 and hand2.compare(hand4) == 1:
        return 210
    elif hand3.compare(hand1) ==1 and hand3.compare(hand2) == 1 and hand3.compare(hand4) == 1:
        return 335
    elif hand4.compare(hand1) ==1 and hand4.compare(hand3) == 1 and hand4.compare(hand2) == 1:
        return 485
    else:
        return 0

hand1image = make_row(Image.open(hand1.hand[0].image_file_name()), 
                      Image.open(hand1.hand[1].image_file_name()), 
                      Image.open(hand1.hand[2].image_file_name()),
                      Image.open(hand1.hand[3].image_file_name()),
                      Image.open(hand1.hand[4].image_file_name()))
hand2image = make_row(Image.open(hand2.hand[0].image_file_name()), 
                      Image.open(hand2.hand[1].image_file_name()), 
                      Image.open(hand2.hand[2].image_file_name()),
                      Image.open(hand2.hand[3].image_file_name()),
                      Image.open(hand2.hand[4].image_file_name()))
hand3image = make_row(Image.open(hand3.hand[0].image_file_name()), 
                      Image.open(hand3.hand[1].image_file_name()), 
                      Image.open(hand3.hand[2].image_file_name()),
                      Image.open(hand3.hand[3].image_file_name()),
                      Image.open(hand3.hand[4].image_file_name()))
hand4image = make_row(Image.open(hand4.hand[0].image_file_name()), 
                      Image.open(hand4.hand[1].image_file_name()), 
                      Image.open(hand4.hand[2].image_file_name()),
                      Image.open(hand4.hand[3].image_file_name()),
                      Image.open(hand4.hand[4].image_file_name()))

grid = makegrid(hand1image, hand2image, hand3image, hand4image)

draw = ImageDraw.Draw(grid)
font = ImageFont.load_default()

draw.text((550, 75)  , hand1.get_hand_type(), font=font, anchor="ms", fill = (255,255,255))
draw.text((550, 200)  , hand2.get_hand_type(), font=font, anchor="ms", fill = (255,255,255))
draw.text((550, 325)  , hand3.get_hand_type(), font=font, anchor="ms", fill = (255,255,255))
draw.text((550, 475)  , hand4.get_hand_type(), font=font, anchor="ms", fill = (255,255,255))
draw.text((550, comparefour()), "Winner", font=font, anchor="ms", fill = (255,0,0))

grid.show()