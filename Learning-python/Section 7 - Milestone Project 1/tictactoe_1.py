## Santosh Khadka - Tic Tac Toe Game 

#Globals
row1 = ['-', '-', '-']
row2 = ['-', '-', '-']
row3 = ['-', '-', '-']

def print_start():
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
            return choice.upper()
        else:
            print('Invalid input try again..')
            

def print_board(r1, r2, r3):
    #h_bar = '    -----------'
    h_bar = '    #############'
    h_bar = '    -------------'
    print('      1   2   3')
    print(h_bar)
    print('A:  |',r1[0],'|',r1[1],'|',r1[2],'|')
    print(h_bar)
    print('B:  |',r2[0],'|',r2[1],'|',r2[2],'|')
    print(h_bar)
    print('C:  |',r3[0],'|',r3[1],'|',r3[2],'|')
    print(h_bar)
    print()
    
def get_input():
    #location = input("Input column letter then row number (i.e. c1): ")
    colRow = [0,0]
    x = 0
    while x == 0:
        print("Pick a location to add your piece...")
        location = input("Input column letter then row number (i.e. c1): ")
        if str(location).lower() == "exit":
            quit()
        #print(location[0])
        #print(location[1])
        if ((str(location[0]).lower() == 'a') or (str(location[0]).lower() =='b') or (str(location[0]).lower() =='c')) and ((location[1] == '1') or (location[1] == '2') or (location[1] == '3')):
            break
        else:
            print("Invalid input, try again...")
            
    column = str(location[0].lower())
    if column == 'a':
        column = 1
    elif column == 'b':
        column = 2
    elif column == 'c':
        column = 3    
    row = int(location[1])
    colRow[0] = column
    colRow[1] = row
    return colRow

def replace_board(col, row, choice):
    global row1
    global row2
    global row3
    # if row == 1:
    #     row1[col] = 
    # elif row == 2:
    # elif row == 3:
def reset_board():
    global row1
    global row2
    global row3
    
    row1 = ['-', '-', '-']
    row2 = ['-', '-', '-']
    row3 = ['-', '-', '-']

def end_game(winner):
    if winner != 'computer':
        print("Congratulations you WON!")
    else:
        print("Better luck next time!")
    
    choice = input("Make your next choice:")
    if choice == 1:
        print("Ok, lets play again!")
        reset_board()
        return(print_start())
    elif choice == 2:
        print("Thanks for playing, bye!")
        quit()
    pr
        
        

def main():
    global row1
    global row2
    global row3
    
    x = 0
    piece = print_start()
    #print_start()
    
    while x == 0:
        print_board(row1, row2, row3) 
        print(get_input())
        print()

if __name__ == "__main__":
    main()