
def printBoard(board):
    print("  A B C")
    print("0 " + board["A0"] + " " + board["B0"] + " " + board["C0"])
    print("1 " + board["A1"] + " " + board["B1"] + " " + board["C1"])
    print("2 " + board["A2"] + " " + board["B2"] + " " + board["C2"])


def verifyBoard(board):
    pass


def playTicTacToe():
    print("Hello and welcome to The Amazing Tic Tac Toe App that no one has ever seen before!")

    board = {
        "A0": "_", "A1": "_", "A2": "_", "B0": "_", "B1": "_", "B2": "_", "C0": "_", "C1": "_", "C2": "_"
    }

    printBoard(board)
    gameFinished = False

    while(not gameFinished):
        print("Just in while")
        gameFinished = True


playTicTacToe()
