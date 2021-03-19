## Santosh Khadka
## Python - Warmup Card Game Project
import random

suits = {"Hearts", "Diamonds", "Spades", "Clubs"}
ranks = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"}
# Dictionary for deck
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    '''
    Card: Suit, rank, value
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
# Testing Class
# two_hearts = Card("Hearts", "Two")
three_clubs = Card("Clubs", "Three")
print(three_clubs.value)
# print(values[two_hearts.rank])

class Deck():
    '''
    Instantiate a new deck.
        - Create all 52 Card objects.
        - Hold as a list of Card objects
        - Suggle a Deck through a method call
            - Random library shuffle() function
        - Deal cards from the Deck object
            - Pop method from cards list.
        - Will return Card class object instances, not just normal python data types.
    '''
    def __init__(self): # No user input because every new deck will be the same
        # All 52 cards
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
#new_deck = Deck()
#first_card = new_deck.all_cards[0]
#print(first_card)

print("END TEST")