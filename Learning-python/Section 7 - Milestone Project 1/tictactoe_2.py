## Santosh Khadka - Tic Tac Toe Game

def end_Game():
    print()
    print("Exiting... Thanks for playing, bye!")
    quit()

def end_options():
    pass

def check_input(location):
    if str(location).lower == "exit":
        end_Game()

def check_ifEmpty(location):
    pass 

def check_ifWin():
    pass

def new_game():
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
            return choice.upper()
        elif(str(choice).upper() == "EXIT"):
            end_Game()
        else:
            print('Invalid input try again..')
    

def update_board(location):
    pass

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
    new_game()
    location = get_input()
    #print(len(str(123)))
def main():
    start_game()

if __name__ == "__main__":
    main()