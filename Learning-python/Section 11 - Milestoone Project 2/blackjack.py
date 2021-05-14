## Santosh Khadka - Blackjack Game
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
player_dealer = Player("Dealer", 99999) # 'Automated' dealer


def new_game_intro():
  print("Welcome to text-based Blackjack!")
  while True:
    x = str(input("Enter '1' to begin. Enter '2' to quit: ")).strip()
    if x == '1':
      print()
      print("Game starting...")
      break
    elif x == '2':
      print("Exiting game...")
      exit()
    else:
      print("Wrong input. Try again!")
      continue

def game_logic():
  new_game_intro()

def main():
  global player_one
  global player_dealer
  player_one = Player("One", 5000)
  player_dealer = Player("Dealer", 99999)

  # print(player_one.money) # TESTING

  # New Deck
  new_deck = Deck()
  new_deck.shuffle()

  game_on = True
  round_num = 0

  # Intro to game.
  new_game_intro()

  while game_on:
    bust = False
    round_num += 1
    print("=====================================")
    print("Round :", round_num, "  -  Player Money: $", player_one.money)

    # Total money check
    if player_one.money < 0:
      print("Player one is out of cash! Game Over!")
      game_on = False
      break

    # NEW ROUND - RESET
    player_one_cards = []
    player_dealer_cards = []
    player_one_cardValue = 0
    player_dealer_cardValue = 0
    new_bet = 0
    money_pot = 0     # reset pot on every round

    # Check if player has enough money for initial bet
    if (player_one.money - 500) < 0:
      print("Player one does not have enough cash for the minimum bet! Game Over!")
      game_on = False
      break
    else:
      # Check bet ammount for proper type and within range
      bet_check = True  
      while bet_check:
        new_bet = int(input("Enter the ammount(integer) you would like to bet (500 to your Total money):"))
        if (player_one.money-new_bet) >= 0 and new_bet>=500:
          player_one.money -= new_bet
          money_pot += new_bet
          print("Bet accepted.\n")
          break
        elif new_bet < 500:
          print("Bet is less than required minimum best! Try again.")
          continue
        else:
          print("Bet exceeds total money held. Try again.")
          continue  
      # player_one.money -= 500
    
    print("Player", player_one.name, "has: $",player_one.money)
    print("Pot: $", money_pot)
    print("\n~~ Dealing cards... ~~")
    # print(new_deck.deal_card()) # TESTING
    player_one_cards.append(new_deck.deal_card())   # Card 1 deal
    player_dealer_cards.append(new_deck.deal_card())
    player_one_cards.append(new_deck.deal_card())   # Card 2 deal
    player_dealer_cards.append(new_deck.deal_card())
    # print(len(new_deck.all_cards)) # TESTING - Check how many cards left in deck

    for x in player_one_cards:
      print("Players Card:", x, ", Value:", x.value)     # Print what cards the player got
      # player_one_cardValue += x.value # Add up total value of current cards - bust check
    print()
    temp = 0
    for x in player_dealer_cards:
      if temp == 0:
        print("Dealers Card:", x, ", Value:", x.value)        # 1st dealer card
        temp = 1
      else:
        print("Dealers Card: X")               # 2nd dealer card - not shown to player
      player_dealer_cardValue += x.value # Add up total value of current cards 
    
    print("")
    while True:
      choice_1 = str(input("Would you like to: Hit or Call?")).upper()
      if choice_1 == "HIT":
        print("Player has decided to HIT!\n")
        player_one_cards.append(new_deck.deal_card())
        player_one_cardValue = 0
        for x in player_one_cards:
          print("Players Card:", x, ", Value:", x.value)     # Print what cards the player got
          player_one_cardValue += x.value # Add up total value of current cards - bust check
          # print(player_one_cardValue)
        if player_one_cardValue>21:
          # print(player_one_cardValue)
          print("Player has BUST! Round over!\n")
          print("Player Money: $", player_one.money)
          bust = True
          break
          # quit()
      elif choice_1 == "CALL":
        print("Player has decided to CALL.\n")
        break
      else:
        print("Invalid input. Try again.")

    # BUST CHECK
    if bust == True:
      continue  # Moves onto the next round.

    while player_dealer_cardValue<17:
      print("Dealer hits...")
      player_dealer_cards.append(new_deck.deal_card())
      player_dealer_cardValue = 0
      for x in player_dealer_cards:
        print("Dealers Card:", x, ", Value:", x.value)     # Print what cards the dealer got
        player_dealer_cardValue += x.value # Add up total value of current cards - bust check
        # print(player_dealer_cardValue)
      if player_dealer_cardValue>21:
        print("\nDealer has BUST! Player receives winnings.")
        print("Round over!\n")
        player_one.money += money_pot*2
        print("Player Money: $", player_one.money)
        money_pot = 0
        bust = True
        break
        # Quit()
    
    # BUST CHECK
    if bust == True:
      continue  # Moves onto the next round.

    # END GAME check
    if player_one_cardValue > player_dealer_cardValue:
      print("Player has:", player_one_cardValue, ", Dealer has:", player_dealer_cardValue)
      print("Player 1 has won!")
      print("Winnings given to player.\n")
      player_one.money += money_pot*2
      print("Player Money:", player_one.money)
    elif player_one_cardValue < player_dealer_cardValue:
      print("Player has:,", player_one_cardValue, " Dealer has:", player_dealer_cardValue)
      print("Player 1 has lost!")
      print("Better luck next time!\n")
      print("Player Money:", player_one.money)
    elif player_one_cardValue == player_dealer_cardValue:
      print("Player has:,", player_one_cardValue, " Dealer has:", player_dealer_cardValue)
      print("Game was a draw!")
      print("Bet returned to player.\n")
      player_one.money += money_pot
      print("Player Money: $", player_one.money)
    else:
      print("GAME ERROR - at end game")
    
    # RESET GAME
    bust = True
    # BUST CHECK
    if bust == True:
      continue  # Moves onto the next round.
          
    # break # TESTING - stop after 1 round

if __name__ == '__main__':
  # executes when ran directly
  main()