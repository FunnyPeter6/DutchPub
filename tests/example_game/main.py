import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card():
    # card class 
    # suit, rank, value
    def  __init__(self, suit, rank):
        self.suit =  suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():
    # create deck of cards, shuffle and deal one
    def __init__(self):
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # create the card object
                created_card = Card(suit,rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# create new deck of cards
new_deck = Deck()

# shuffle the new deck
new_deck.shuffle()

# debugging line, prints the whole deck
""" for card_object in new_deck.all_cards:
    print(card_object) """

# trigger the deal one card
my_card = new_deck.deal_one()

# debugging line, prints the popped card
#print(popped_card)

# debugging line, prints the length of the new deck after popping a card
#print(len(new_deck.all_cards))

class Player():
    # player class, has a name, able to remova or add a card to hand, and hold those cards
    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of mutiple card objects
            self.all_cards.extend(new_cards)
        else:
            # for a single card object
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# creates player with name
new_player = Player("Cyperus")

# debugging line, prints the player hand
print(new_player)

# debugging line, adds a card(s) to the player hand
new_player.add_cards([my_card,my_card,my_card,my_card,my_card])

# debugging line, prints wich card is added
print(my_card)

# debugging line, print player again
print(new_player)

# removes a card from player's hand
new_player.remove_one()

# debugging line, print player
print(new_player)