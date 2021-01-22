## Santosh Khadka - Tic Tac Toe Game

## Globals
game_reset = 0
player = 'a'
row1 = ['-', '-', '-']
row2 = ['-', '-', '-']
row3 = ['-', '-', '-']
    
def end_Game():
    print()
    print("Exiting... Thanks for playing, bye!")
    quit()

def end_options():
    x = 0
    while x==0: 
        choice = str(input("Enter 1 to play again or 2 to exit: ").strip())
        if (choice == '1'):
            print("You chose to play again.. resetting game!")
            return choice
        elif (choice == '2'):
            print("You chose to exit game.")
            end_Game()
        else:
            print("Invalid input, try again!")
    

def check_input(location):
    if str(location).lower == "exit":
        end_Game()

def check_ifEmpty(location):
    location = str(location)
    row = int(location[0])
    column = int(location[1])
    if (row == 1):
        if str(row1[column]) != '-':
            return 'notempty'
    elif (row == 2):
        if str(row2[column]) != '-':
            return 'notempty'
    elif (row == 3):
        if str(row3[column]) != '-':
            return 'notempty'
    return 'empty' 

def check_ifWin():
    pass

def new_game():
    global player
    print("===============================")
    print('    Lets play Tic-Tac-Toe!')
    print("===============================")
    print("[Type 'exit' to leave anytime.]")
    print()
    x = 0
    while x == 0:
        choice = input("Would you like to be X or O?")
        if (choice == 'x') or (choice == 'X') or (choice == 'o') or (choice == 'O'):
            print()
            print("You choose", choice.upper(), ", great! Lets start:")
            player = choice.upper() 
            return choice.upper()
        elif(str(choice).upper() == "EXIT"):
            end_Game()
        else:
            print('Invalid input try again..')
    

def update_board(location):
    global player
    location = str(location)
    row = int(location[0])
    column = int(location[1])
    if (row == 1):
        row1[column] = player
    elif (row == 2):
        row2[column] = player
    elif (row == 3):
        row1[column] = player
    else:
        print("ERROR UPDATING BOARD")

def get_input():
    x = 0
    while x == 0:
        print("Pick a empty location to add your piece...")
        location = input("Input column # then row # (i.e. 31): ")
        if str(location).lower() == "exit":
            end_Game()
        if ((str(location[0]) == '1') or (str(location[0]) == '2') or (str(location[0]) == '3')) and ((str(location[1]) == '1') or (str(location[1]) == '2') or (str(location[1]) == '3')):
            if(len(str(location)) < 3):
                break
            else:
                print("Invalid input, try again...")
        else:
            print("Invalid input, try again...")
    return location

def start_game():
    #new_game()
    #location = get_input()
    end_options()
    #print(len(str(123)))

def main():
    start_game()

if __name__ == "__main__":
    main()