## Santosh Khadka
# Testing for war_game.py

import war_game

def test_card():
    two_hearts = war_game.Card("Hearts", "Two")
    three_clubs = war_game.Card("Clubs", "Three")
    print(three_clubs.value) 
    print(war_game.values[two_hearts.rank])

def test_deck():
    new_deck = war_game.Deck()
    print("Deck Length:", len(new_deck.all_cards), '\n')
    
    #first_card = new_deck.all_cards[0]
    #print(first_card)

    for card in new_deck.all_cards: # to print all cards
        print(card)
    new_deck.shuffle()  # shuffle the new_deck list aka shuffling the play deck
    print("\n=============AFTER SHUFFLE=============\n")
    for card in new_deck.all_cards: # to print all cards
        print(card)

    print("============================================")
    new_card = new_deck.deal_one()
    print("New Card:", new_card)
    print("Deck Length:", len(new_deck.all_cards))
    
    print("END TEST")

def test_player():
    player_santosh = war_game.Player("Santosh")
    print(player_santosh)   # 0 cards
    
    two_hearts = war_game.Card("Hearts","Two")
    #print(two_hearts)
    player_santosh.add_cards(two_hearts)
    print(player_santosh)   # 1 cards

    player_santosh.add_cards([two_hearts, two_hearts, two_hearts])
    print(player_santosh)   # 4 cards (1+3)

def main():
    deck_1 = war_game.Deck()
    # test_player()
    test_card()
    
if __name__ == "__main__":
    main()