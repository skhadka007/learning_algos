## Santosh Khadka - Tic Tac Toe Game

import time
import random
 
## Globals
game_reset = 0
player = 'a'
player2 = 'a'
check_full = 0 # counter to see if board is full. Full at 9.
row1 = ['-', '-', '-']
row2 = ['-', '-', '-']
row3 = ['-', '-', '-']

def reset_game():
    '''
    Returns 'true' or 'false'
        Resets game.
            resets board to '-'
            resets player and player2 to 'a'
    '''
    global row1; global row2; global row3
    global player; global player2
    global check_full
    
    row1 = ['-', '-', '-']
    row2 = ['-', '-', '-']
    row3 = ['-', '-', '-']
    player = 'a'
    player2 = 'a'
    check_full = 0
   
def end_Game():
    '''
    No return type - endsgame.
        Prints end game message and ends program.
    '''
    print()
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("Exiting... Thanks for playing, bye!")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print()
    quit()

def end_options():
    '''
    Returns 1 if play again - also resets game.
        Asks user to pick 1 to play again or 2 to exit.
            Verifies input.
            Resets board if 1 and returns 1.
            Ends program if choice is 2. 
    '''
    x = 0
    while x==0: 
        choice = str(input("Enter 1 to play again or 2 to exit: ").strip())
        if (choice == '1'):
            print()
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("You chose to play again... resetting game!")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print()
            reset_game()
            return choice
        elif (choice == '2'):
            print("You chose to exit game.")
            end_Game()
        else:
            print("Invalid input, try again!")

def check_input(location):
    '''
    No return type - ends game.
        Checks to see if user entered 'exit'
    '''
    choice = str(location).lower()
    choice = choice.strip()
    if choice == "exit":
        end_Game()

def check_ifEmpty(location):
    '''
    Returns 'notempty' or 'empty'
        Checks board to verify that location is empty
    '''
    location = str(location)
    row = int(location[0]) - 1
    column = int(location[1]) - 1
    if (row == 0):
        if str(row1[column]) != '-':
            return 'notempty'
    elif (row == 1):
        if str(row2[column]) != '-':
            return 'notempty'
    elif (row == 2):
        if str(row3[column]) != '-':
            return 'notempty'
    return 'empty' 

def check_ifWin():
    '''
    Returns winner: 'X' or 'O' or 'nowin' or 'tie'(when board is full)
        Checks entire board horizontally, vertically, and diagonally to see if anyone won.
    '''
    # Player O win checks
    if (row1[0]=='O' and  row1[1]=='O' and row1[2]=='O'):   #horizontals
        return 'O'
    elif (row2[0]=='O' and  row2[1]=='O' and row2[2]=='O'):
        return 'O'
    elif (row3[0]=='O' and  row3[1]=='O' and row3[2]=='O'):
        return 'O'
    elif (row1[0]=='O' and  row2[0]=='O' and row3[0]=='O'): #verticals 
        return 'O'
    elif (row1[1]=='O' and  row2[1]=='O' and row3[1]=='O'): 
        return 'O'
    elif (row1[2]=='O' and  row2[2]=='O' and row3[2]=='O'): 
        return 'O'
    elif (row1[0]=='O' and  row2[1]=='O' and row3[2]=='O'): #diagonals 
        return 'O'
    elif (row1[2]=='O' and  row2[1]=='O' and row3[0]=='O'): 
        return 'O'
    # Player X win checks
    elif (row1[0]=='X' and  row1[1]=='X' and row1[2]=='X'): #horizontals
        return 'X'
    elif (row2[0]=='X' and  row2[1]=='X' and row2[2]=='X'):
        return 'X'
    elif (row3[0]=='X' and  row3[1]=='X' and row3[2]=='X'):
        return 'X'
    elif (row1[0]=='X' and  row2[0]=='X' and row3[0]=='X'): #verticals 
        return 'X'
    elif (row1[1]=='X' and  row2[1]=='X' and row3[1]=='X'): 
        return 'X'
    elif (row1[2]=='X' and  row2[2]=='X' and row3[2]=='X'): 
        return 'X'
    elif (row1[0]=='X' and  row2[1]=='X' and row3[2]=='X'): #diagonals 
        return 'X'
    elif (row1[2]=='X' and  row2[1]=='X' and row3[0]=='X'): 
        return 'X'
    else:
        if check_full == 9:
            return 'tie'
        return 'nowin'

def new_game():
    '''
    Returns 'X' or 'O'
        Starts new TicTacToe game
            Prints intro text.
            Asks user to pick X or O (char).
                Verifies input validity
                Sets computer as the other piece.
            Exits game player enters exit
    '''
    global player; global player2
    
    print("===============================")
    print('    Lets play Tic-Tac-Toe!')
    print("===============================")
    print("[Type 'exit' to leave anytime.]")
    print()
    x = 0
    while x == 0:
        choice = input("Would you like to be X or O?")
        if (choice == 'x') or (choice == 'X') or (choice == 'o') or (choice == 'O'):
            time.sleep(0.7)
            print("===============================")
            print("You choose", choice.upper(),", great! Lets start:")
            print("===============================")
            player = choice.upper()
            player2 = 'O' if player == 'X' else 'X' # Sets computer as the other piece.
            return choice.upper()
        elif((str(choice).upper()).strip() == "EXIT"):
            end_Game()
        else:
            time.sleep(0.5)
            print('Invalid input try again..')
    

def update_board(location, who):
    '''
    No return - updates board.
        Updates board with users location choice.
            Prints error message if update did not work.
    '''
    global row1; global row2; global row3
    global check_full
    piece = player
    
    if who == "comp":
        piece = player2
    
    location = str(location)
    row = int(location[0]) - 1
    column = int(location[1]) - 1
    if (row == 0):
        row1[column] = piece
        check_full += 1
    elif (row == 1):
        row2[column] = piece
        check_full += 1
    elif (row == 2):
        row3[column] = piece
        check_full += 1
    else:
        print("ERROR UPDATING BOARD")

def get_input():
    '''
    Returns location(int - example: 21)
        Get player input for a board space.
            Will exit if user types 'exit'
            Will say invalid input if out of bounds.
    '''
    x = 0
    while x == 0:
        print("Pick a empty location to add your piece...")
        location = input("Input row # then column # (i.e. 13 for top right corner): ")
        length = len(str(location).strip())
        if (str(location).lower()).strip() == "exit":
            end_Game()
        if (length < 2):
            print("Invalid input, try again...")
            time.sleep(0.5)
        elif ((str(location[0]) == '1') or (str(location[0]) == '2') or (str(location[0]) == '3')) and ((str(location[1]) == '1') or (str(location[1]) == '2') or (str(location[1]) == '3')):
            if(length < 3):
                if check_ifEmpty(location) == 'empty':
                    break
                else:
                    print("Invalid location, try again...")
                    time.sleep(0.5)
            else:
                print("Invalid input, try again...")
                time.sleep(0.5)
        else:
            print("Invalid input, try again...")
            time.sleep(0.5)
    return location

def print_board():
    '''
    No return.
        Prints current board.
    '''
    #h_bar = '    -----------'
    h_bar = '         -------------'
    print("      ---CURRENT BOARD---")
    print('           1   2   3')
    print(h_bar)
    print('     1:  |',row1[0],'|',row1[1],'|',row1[2],'|')
    print(h_bar)
    print('     2:  |',row2[0],'|',row2[1],'|',row2[2],'|')
    print(h_bar)
    print('     3:  |',row3[0],'|',row3[1],'|',row3[2],'|')
    print(h_bar)
    print()

def computer_pick():
    '''
    No return.
        Computer picks an empty board space.
        Uses random number generator
    '''
    print("Computer picking location... updating board...")
    time.sleep(1.2)
    # prints a random value from the list
    list1 = [1, 2, 3]
    while True:
        comp_pick = str(random.choice(list1)) + str(random.choice(list1))
        if (check_ifEmpty(comp_pick) == 'empty'):
            update_board(comp_pick, "comp")
            break
    
def game_complete(winner):
    '''
    No return.
        Output when there is a winner or a tie.
    '''
    if winner == player:
        print("+-++-+ Congratulations you WON! +-++-+")
    elif winner == 'tie':
        print("+-++-+ Tie game, better luck next time! +-++-+")
    else:
        print("+-++-+ You lost, better luck next time! +-++-+")
    
def start_game():
    '''
    No return.
        Structure for a full new game.
    '''
    x = 0
    new_game()
    print_board()
    while x == 0:    
        #time.sleep(2)
        location = get_input()
        print("Updating board...")
        time.sleep(0.3)
        update_board(location, "player")
        print_board()
        check = check_ifWin()
        if (check == 'nowin'):
            computer_pick()
            print_board()
        check = check_ifWin()
        if (check == 'nowin'):
            continue
        else:
            break
    game_complete(check)
    #end_options()

def main():
    while True:        
        start_game()
        end_options()

    
if __name__ == "__main__":
    main()