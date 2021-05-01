## Santosh Khadka
# Blackjack Game
'''
Complete(text) Blackjack card game using Python
Requirements:
    - Need to create a simple text-based BlackJack game
    - Needs to have one player versus an automated dealer.
    - Player can stand or hit.
    - Player must be able to pick their betting amount.
    - Need to keep track of the player's total money.
    - Need to alert the player of wins, losses, or busts, etc...

    -**Must use OOP and classes in some portion of your game. 
      You can not just use functions in your game. 
      Use classes to help you define the Deck and the Player's hand. 
      There are many right ways to do this, so explore it well!
'''
import random
import pdb

# Standard playing card deck - no jokers
suits = {"Hearts", "Diamonds", "Spades", "Clubs"}
ranks = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"}

rank_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack': 10, 'Queen':10, 'King':10, 'Ace': 11}
# Need to adjust for Ace - 1 or 11

class Card():
  '''
  Card class. 
    Instantiate a card.
    Card value: Suit, rank, value
  '''
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = rank_values[rank]

  def __str__(self):
    return self.rank + " of " + self.suit

class Deck():
  '''
  Instantiate a new deck.
    - 52 Card deck/objects.
    - List of Card objects.
    - Shuffle deck through a method call.
      - Random library shuffle function.
    - Deal cards from Deck object
      - Pop method from cards list.
    - Will return Card class object instances, not just normal python data types.
  '''
  def __init__(self):
    self.all_cards = []
    for suit in suits:
      for rank in ranks:
        created_card = Card(suit, rank) # Creates Card object with the suit & rank
        self.all_cards.append(created_card) # Appends newly created Card object to all_cards list
  
  def shuffle(self):
    random.shuffle(self.all_cards)  # Shuffles the list around
  
  def deal_card(self):
    return self.all_cards.pop()

class Player:
  '''
  Player class
  '''
  def __init__(self, name, money):
    self.name = name
    self. all_cards = []
    self.money = money
  
  def add_cards(self, new_cards):
    if type(new_cards) == type([]):
      self.all_cards.extend(new_cards)
    else:
      self.all_cards.append(new_cards)

  def change_money(self, money):
    self.money += money

# Players
player_one = Player("One", 5000)
player_dealer = Player("Dealer", 99999)
# Automated dealer

def new_game_intro():
  print("Welcome to Blackjack!")

def game_logic():
  new_game_intro()

def main():
  global player_one
  global player_dealer
  player_one = Player("One", 5000)
  player_dealer = Player("Dealer", 99999)

  money_pot = 0

  # print(player_one.money) # TESTING

  # New Deck
  new_deck = Deck()
  new_deck.shuffle()

  game_on = True
  round_num = 0

  while game_on:
    round_num += 1
    print("=====================================")
    print("Round :", round_num)

    # Total money check
    if player_one.money <= 0:
      print("Player one is out of cash! Game Over!")
      game_on = False
      break

    # NEW ROUND
    player_one_cards = []
    money_pot += 500

    if (player_one.money - 500) <= 0:
      print("Player one does not have enough cash for the minimum bet! Game Over!")
      game_on = False
      break
    else:
      player_one.money -= 500
    
    print("Player", player_one.name, "has: $",player_one.money)
    print("Pot: $", money_pot)
    print("\n~~ Dealing cards... ~~")
    # print(new_deck.deal_card()) # TESTING
    player_one_cards.append(new_deck.deal_card())
    player_one_cards.append(new_deck.deal_card())
    # print(len(new_deck.all_cards)) # TESTING - Check how many cards left in deck
    for x in player_one_cards:
      print(x, "Value:", x.value)
    
    

    break # TESTING

if __name__ == '__main__':
  # executes when ran directly
  main()