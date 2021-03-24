## Santosh Khadka
## Python - Warmup Card Game Project
import random
import pdb

suits = {"Hearts", "Diamonds", "Spades", "Clubs"}
ranks = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"}
# Dictionary for deck
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

## CLASSES
class Card:
    '''
    Instantiate a card.
        Card: Suit, rank, value
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

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

    def shuffle(self):
        random.shuffle(self.all_cards) # shuffles the dictionary around

    def deal_one(self):
        # Because we 'deal one card' were techincally removing it from the list of all_cards -> pop
        # The pop() method removes the item at the given index from the list and returns the removed item.
        # argument passed to method is optional. Default index -1 is passed as an argument (index of the last item).
        return self.all_cards.pop()

class Player:
    '''
    Instantiate a player.
        - Hold instances of Cards.
        - Add and remove cards from hand.
        - Flexible: add one or many cards.
    '''
    def __init__(self, name):
        self.name = name
        self.all_cards = [] # new player has no cards
    
    def remove_one(self):
        # Use pop to remove
        return self.all_cards.pop()

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        string1 = "Player " + str(self.name) + " has " + str(len(self.all_cards)) + " card(s)."
        return string1

## LOGIC
def logic_new_game():
    # New players
    global player_one
    global player_two
    player_one = Player("One")
    player_two = Player("Two")
    
    # New deck
    new_deck = Deck()
    new_deck.shuffle()

    # Splitting deck between 2 players
    deck_half = int(len(new_deck.all_cards)/2)
    for x in range(deck_half):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
    
    #print(len(player_one.all_cards))
    #print(len(player_two.all_cards))

def main():
    logic_new_game()

    global player_one
    global player_two

    game_on = True
    round_num = 0

    while game_on:

        round_num += 1
        print("Round: ", round_num)

        # Out of cards check
        if len(player_one.all_cards) == 0:
                print("Player One out of cards! Game Over!")
                print("Player Two Wins!")
                game_on = False
                break
        
        break # for testing
    
if __name__ == "__main__":
    main()