''' We will make the board using dictionary
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move
    we will change the value according to player's choice of move. '''

theBoard = {'7': '.' , '8': '.' , '9': '.' ,
            '4': '.' , '5': '.' , '6': '.' ,
            '1': '.' , '2': '.' , '3': '.' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['1'] + ' ' + board['2'] + ' ' + board['3'])
    print(board['4'] + ' ' + board['5'] + ' ' + board['6'])
    print(board['7'] + ' ' + board['8'] + ' ' + board['9'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    count = 0
    print("Enter a name for the X player:")
    x=input()
    print("Enter a name for the O player:")
    o=input()

    f=1

    while f==1:
          print("Who plays first, "+ x +" or " + o + " ?")
          turn=input()
          if turn==x or turn==o:
              f=0
          else:
              print(turn + " is not a registered player.")
    print("Board: \n1 2 3\n4 5 6\n7 8 9\n")

    for i in range(10):
        printBoard(theBoard)
        print("Player of current turn: " + turn)

        if turn==x:
            a='X'
        else:
            a='O'

        f=0
        while f==0:
            print("\nEnter a number (1 to 9):")
            move=input()
            if move=='1' or move=='2'or move=='3' or move=='4' or move=='5' or move=='6' or move=='7' or move=='8' or move=='9':
                f=1
            else:
                print("Invalid number")
            if f==1:
                if theBoard[move] == '.':
                    theBoard[move] = a
                    count += 1
                else:
                    print("That place is already filled.\nMove to which place?")
                    f=0
                    continue



        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != '.': # across the top
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != '.': # across the middle
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != '.': # across the bottom
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != '.': # down the left side
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != '.': # down the middle
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != '.': # down the right side
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != '.': # diagonal
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != '.': # diagonal
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break

        # Now we have to change the player after every move.
        if turn == x:
            turn = o
        else:
            turn = x

    # Now we will ask if player wants to restart the game or not.
    e=0
    while e==0:
        restart = input("Would you like to play again? (y/n)")
        if restart == "y" or restart == "Y":
            for key in board_keys:
                theBoard[key] = "."
            e=1
            game()
        elif restart!="n" and restart!="N":
            print("Invalid entry")
        elif restart=="n" or restart=="N":
            break




if __name__ == "__main__":
    game()
