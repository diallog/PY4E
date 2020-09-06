#!/usr/bin/env python3

# PURPOSE: practice top-down design and implmenetation by building a game

from random import choice


def ContinueGame(current_score, goal_score=100):
    # Return FALSE if game should end, TRUE if game is not over
    if (current_score >= goal_score):
        return False
    else:
        return True


def ConvertLetterToCol(Col):
    if Col == 'a':
        return 0
    elif Col == 'b':
        return 1
    elif Col == 'c':
        return 2
    elif Col == 'd':
        return 3
    elif Col == 'e':
        return 4
    elif Col == 'f':
        return 5
    elif Col == 'g':
        return 6
    elif Col == 'h':
        return 7
    else:
        # not a valid column
        return -1


def DoRound(board):
    # Perform one round of the game
    # Display current board
    DrawBoard(board)
    # Get move
    move = GetMove()
    # Update DrawBoard
    Update(board, move)
    # update turn number
    global turn
    turn += 1


def DrawBoard(board):
    # Display the board to the screen
    linetodraw = ""
    # Draw some blank lines for separation
    print("\n\n\n")
    print("-----------------------------------")
    # Draw rows top down (8 to 1)
    for i in range(7, -1, -1):
        # Draw each rows
        linetodraw = ""
        linetodraw += str(i+1)
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw += " |"
        print(linetodraw)
        print("-----------------------------------")
    print("    a   b   c   d   e   f   g   h")
    global score
    print("\nCurrent Score: ", score)


def DropPieces(board):
    # Fill blanks with random pieces
    for j in range(8):
        # make a list of the piecces in the columns
        listofpieces = []
        for i in range(8):
            if board[i][j] != 0:
                listofpieces.append(board[i][j])
        # copy that list into the column
        for i in range(len(listofpieces)):
            board[i][j] = listofpieces[i]
        # fill in remainder of column with 0s
        for i in range(len(listofpieces), 8):
            board[i][j] = 0


def FillBlanks(board):
    # Fill blanks with random pieces
    for i in range(8):
        for j in range(8):
            if (board[i][j] == 0):
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])


def GetMove():
    # Get the move from the user
    move = input("Enter move: ")

    # loop until game receives a valid move
    while not IsValid(move):
        move = input("That's not a valid move! Enter another move: ")
    return move


def InitializeGrid(board):
    # Initialize grid utilizing random values
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])


def Initialize(board):
    # Initialize game
    # Initilize grid
    InitializeGrid(board)
    # Initilize score
    global score
    score = 0
    # Initilize turn number
    global turn
    turn = 1


def IsValid(move):
    # Returns true if the move is valid, false otherwise
    # Check length of move
    if len(move) != 3:
        return False

    # CHeck that the space and direction are valid
    if not (move[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        return False
    if not (move[1] in ['1', '2', '3', '4', '5', '6', '7', '8']):
        return False
    if not (move[2] in ['u', 'd', 'l', 'r']):
        return False

    # Check that the direction is valid for the given row / column
    # Check that first column moves do not go left
    if (move[0] == 'a') and (move[2] == 'l'):
        return False
    # Check that last column moves do not go right
    if (move[0] == 'h') and (move[2] == 'r'):
        return False
    # Check that bottom row moves do not go down
    if (move[1] == '1') and (move[2] == 'd'):
        return False
    # Check that top row moves do not go up
    if (move[0] == '8') and (move[2] == 'u'):
        return False

    # no problems found, so the move is valid
    return True


def RemovePieces(board):
    # Remove 3-in-a-row and 3-in-a-column pieces
    # Create board to store remove or not
    remove = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0], ]

    # Go through rows
    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j+2]):
                # three in a row are the same!
                remove[i][j] = 1
                remove[i][j+1] = 1
                remove[i][j+2] = 1

    # Go through columns
    for j in range(8):
        for i in range(6):
            if (board[i][j] == board[i+1][j]) and (board[i][j] == board[i+2][j]):
                # three in a row are the same!
                remove[i][j] = 1
                remove[i+1][j] = 1
                remove[i+2][j] = 1

    # Elimiate marked locations
    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if remove[i][j] == 1:
                board[i][j] = 0
                score += 1
                removed_any = True
    return removed_any


def SwapPieces(board, move):
    # Swap pieces on board according to move
    # Get original postion
    origrow = int(move[1])-1
    origcol = ConvertLetterToCol(move[0])

    # Get adjacent postion
    if move[2] == 'u':
        newrow = origrow + 1
        newcol = origcol
    elif move[2] == 'd':
        newrow = origrow - 1
        newcol = origcol
    elif move[2] == 'l':
        newrow = origrow
        newcol = origcol - 1
    elif move[2] == 'r':
        newrow = origrow
        newcol = origcol + 1

    # Swap objects in two positions
    temp = board[origrow][origcol]
    board[origrow][origcol] = board[newrow][newcol]
    board[newrow][newcol] = temp


def Update(board, move):
    # Update board according to move
    SwapPieces(board, move)
    pieces_eliminated = True
    while pieces_eliminated:
        pieces_eliminated = RemovePieces(board)
        DropPieces(board)
        FillBlanks(board)


def Main():
    # Define variables
    score = 0
    turn = 0
    goalscore = 100
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0], ]

    # Initialize game
    Initialize(board)

    # Loop while game not over
    while ContinueGame(score, goalscore):
        # Do round of game
        DoRound(board)


if __name__ == '__main__':
    Main()
