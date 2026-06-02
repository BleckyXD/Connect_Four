from logging.config import stopListening

boardInfo = [[" " for _ in range(7)] for _ in range(6)]

class ColumnFullError(Exception):
    pass

def playerTurn(player):
    row = 5
    column = (int(input("Choose Column:"))) - 1

    # row and column
    # boardInfo[2][1] = "X"

    if boardInfo[row][column] == " ":
        boardInfo[row][column] = player
    else:
        while boardInfo[row][column] != " ":
            row -= 1
            if row == -1:
                raise ColumnFullError("Error!")
        boardInfo[row][column] = player

def playerO():
    row = 5
    column = (int(input("Choose Column:"))) - 1

    if boardInfo[row][column] == " ":
        boardInfo[row][column] = "O"
    else:
        while boardInfo[row][column] != " ":
            row -= 1
            if row == -1:
                raise ColumnFullError("Error!")
        boardInfo[row][column] = "O"

def boardGame():
    for i in range(7):
        print(f"  {i + 1} ", end="")

    print()
    for i in range(6):
        print("+---" * 7 + "+")

        for a in range(3):
            for p in range(7):
                if a == 1:
                    print(f"| {boardInfo[i][p]} ", end="")
                else:
                    print(f"|   ", end="")
            print("|")
    print("+---" * 7 + "+")

def rightToLeftWin(player):
    winner = False
    winCount = 0
    for i in range(5, -1, -1):
        for a in range(6, -1, -1):
            if boardInfo[i][a] == player:

                winCount += 1
                if winCount == 4:
                    print(f"Player {player} is the winner!")
                    winner = True
            else:
                winCount = 0
    return winner

def downToUpWin(player):
    winner = False
    winCount = 0
    for a in range(6, -1, -1):
        for i in range(5, -1, -1):
            if boardInfo[i][a] == player:

                winCount += 1
                if winCount == 4:
                    print(f"Player {player} is the winner!")
                    winner = True
            else:
                winCount = 0

    return winner

def leftToRightDiagonalWin(player):
    winner = False
    winCount = 0
    diagonalCount = 0

    for i in range(5, -1, -1):
        if boardInfo[i][diagonalCount] == player:
            winCount += 1
            if winCount == 4:
                print(f"Player {player} is the winner!")
                winner = True
        else:
            winCount = 0
        diagonalCount += 1
    return winner

def rightToLeftDiagonalWin(player):
    winner = False
    winCount = 0
    diagonalCount = 6
    for i in range(5, -1, -1):
        if boardInfo[i][diagonalCount] == "X":
            winCount += 1
            if winCount == 4:
                print(f"Player {player} is the winner!")
                winner = True
        else:
            winCount = 0
        diagonalCount -= 1
            #This is the only addition that will give you the right number
            #Its like to say that the mathematical formula is a different description of that cell
            #Aside from its real number, the formula is a different description of the same area, ONLY for that area
            #Problem with this. It can read diagonal, but the win count will be reset since we are checking the whole board
            # if (boardInfo[i][a] == "X"):
            #     if i == (a - 1):
            #         print(f"row: {i}, column: {a}")
            #         winCount += 1
            #         if winCount == 4:
            #             print("winner!")
            #             winner = True
            #     else:
            #         winCount = 0

    return winner

X = "X"
O = "O"
rlWin = False
duWin = False
lrdWin = False
rldWin = False

while not (rlWin or duWin or lrdWin or rldWin):

    boardGame()

    try:
        #pass in the function the X or O
        playerTurn(X)

        rlWin = rightToLeftWin(X)

        duWin = downToUpWin(X)

        lrdWin = leftToRightDiagonalWin(X)

        rldWin = rightToLeftDiagonalWin(X)

        boardGame()

        if (rlWin == False) and (duWin == False) and (lrdWin == False) and (rldWin == False):
            playerTurn(O)

            rlWin = rightToLeftWin(O)

            duWin = downToUpWin(O)

            lrdWin = leftToRightDiagonalWin(O)

            rldWin = rightToLeftDiagonalWin(O)

    except IndexError:
        print("Not a valid Column!")

    except ColumnFullError as message:
        print(f"{message} Choose another column!")






























# for a in range(7):
#     print("+---", end="")
# print("+---" * 7 + "+")



# for i in range (6):
#
#     for e in range (3):
#
#         for f in range (8):
#             print("|   ", end="")
#
#         print()
#
#     for a in range (7):
#       print("+---", end="")
#       if a == 6:
#           print("+")


# This is exactly what Line 2 is doing under the hood:
# r = []
# for x in a:                 # Outer loop
#     for _ in range(2):      # Inner loop
#         r.append(x)         # Output expression
# print(r)


# print(r)

# z = []
#
# for _ in range(7):
#     row = []
#     for _ in range(6):
#         row.append(" ")
#     z.append(row)
# print(z)
# USE MATHEMATICAL FORMULA FOR CHECKING THE CELLS