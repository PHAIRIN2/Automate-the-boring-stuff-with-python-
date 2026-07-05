# A Tic-Tac-Toe Board

Theboard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}

def printBoard(board):
    print(board["top-L"] + " | " + board["top-M"] + "| " + board["top-R"])
    print("--+--+--")
    print(board["mid-L"] + " | "+ board["mid-M"] + "| " + board["mid-R"])
    print("--+--+--")
    print(board["low-L"] + " | " + board["low-M"] + "| " + board["low-R"])

turn = "X"
for i in range(9):
    printBoard(Theboard)
    print("Turn for:", turn, "Move no which spase?")
    if turn == "":
        break
    Move = input()
    Theboard[Move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

printBoard(Theboard)
