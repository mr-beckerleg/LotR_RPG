import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hearts = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"]
spades = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"]
clubs = ["AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"]
hand = []

draw_deck = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"]

discard_pile = []

def deal():
    new_card = random.choice(draw_deck)
    draw_deck.remove(new_card)

def draw_from_deck():
    new_card = random.choice(draw_deck)
def draw_from_discard():
    new_card = (int(input("What card do you want? ")), len(discard_pile) + 1)


    
class player:
    def __init__(self, name):
        self.name = name
        self.hand = hand
    def my_hand(self):
        

class computer_player:
    def __init__(self):
        self.hand = hand
    def hand(self):
        

p1 = player("Sean")

print(draw_deck)
print(discard_pile)
print(p1.hand)
  
#while diamonds:
#    next_turn = input("Press enter to pick a card, or Q then enter to quit: ")
#    if next_turn == "":
#        new_card = random.choice(diamonds)
#        hand.append(new_card)
#        diamonds.remove(new_card)
#    if next_turn == "Q":
#        quit()
#    print(f'''Your Hand: {hand}
#    Remaining cards: {diamonds}''')

#if not diamonds:
#        print("There are no more cards to pick.")

