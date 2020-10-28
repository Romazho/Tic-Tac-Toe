import random
import string


def printBoard(board):
    print("  A B C")
    print("0 " + board["A0"] + " " + board["B0"] + " " + board["C0"])
    print("1 " + board["A1"] + " " + board["B1"] + " " + board["C1"])
    print("2 " + board["A2"] + " " + board["B2"] + " " + board["C2"])


def verifyClientInput(input, board):
    if(input in board or input == "Q"):
        return True
    return False


def takeClientInput():
    clientInput = input("Enter your desired position or 'Q' to quit:")
    return clientInput.upper()


def verifyBoard(clientPositions):
    if "A0" in clientPositions:
        if "A1" in clientPositions:
            if "A2" in clientPositions:
                return True
        if "B0" in clientPositions:
            if "C0" in clientPositions:
                return True
        if "B1" in clientPositions:
            if "C2" in clientPositions:
                return True

    if "B1" in clientPositions:
        if "C0" in clientPositions:
            if "A2" in clientPositions:
                return True
        if "B0" in clientPositions:
            if "B2" in clientPositions:
                return True
        if "A1" in clientPositions:
            if "C1" in clientPositions:
                return True

    if "C2" in clientPositions:
        if "C1" in clientPositions:
            if "C0" in clientPositions:
                return True
        if "B2" in clientPositions:
            if "A2" in clientPositions:
                return True

    return False


def computerRandomPlay(takenPositionsInBoard):
    position = takenPositionsInBoard[0]
    # will always be true at the begining, because the client always starts first. "test change"
    while position in takenPositionsInBoard:
        number = random.randint(0, 2)
        letter = random.choice(string.ascii_letters[0:3])
        position = (letter + str(number)).upper()

    print("Computer position: " + position)
    return position


def playTicTacToe():
    print("Hello and welcome to The Amazing Tic Tac Toe Game that no one has ever seen before!")

    board = {
        "A0": "_", "A1": "_", "A2": "_", "B0": "_", "B1": "_", "B2": "_", "C0": "_", "C1": "_", "C2": "_"
    }

    takenPositionsInBoard = []
    clientPositions = []
    ComputerPositions = []
    clientIsWinner = False
    computerIsWinner = False
    gameIsAtie = False
    numberOfTurns = 0

    printBoard(board)
    gameFinished = False
    clientInput = ""

    while(not gameFinished):
        clientInput = takeClientInput()

        while(not verifyClientInput(clientInput, board)):
            print("Invalid character.")
            clientInput = takeClientInput()

        while (clientInput in takenPositionsInBoard):
            print("This position is taken")
            clientInput = takeClientInput()

        if clientInput == "Q":
            break

        takenPositionsInBoard.append(clientInput)
        clientPositions.append(clientInput)

        board[clientInput] = "X"
        printBoard(board)

        gameFinished = verifyBoard(clientPositions)
        numberOfTurns += 1
        print("Number of turns: " + str(numberOfTurns))

        if gameFinished:
            clientIsWinner = True
            break
        elif numberOfTurns == 9:
            gameIsAtie = True
            break
        else:
            computerPosition = computerRandomPlay(takenPositionsInBoard)

        ComputerPositions.append(computerPosition)
        takenPositionsInBoard.append(computerPosition)
        board[computerPosition] = "O"
        printBoard(board)

        gameFinished = verifyBoard(ComputerPositions)
        numberOfTurns += 1
        print("Number of turns: " + str(numberOfTurns))

        if gameFinished:
            computerIsWinner = True
            break

    if(gameIsAtie):
        print("Wow it's a tie!")
    elif(clientIsWinner):
        print("Congratulations! You won!!")
    elif(computerIsWinner):
        print("Oops, looks like you lost.")


def main():

    clientAnswer = input("Would you like to play Tic Tac Toe? y/n :")

    while (clientAnswer != "n"):

        if(clientAnswer == "y"):
            playTicTacToe()
        else:
            print("Invalid input!")

        clientAnswer = input("Would you like to play Tic Tac Toe? y/n :")

    print("Goodbye!")


main()
