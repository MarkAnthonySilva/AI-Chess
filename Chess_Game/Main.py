
import tkinter as tk
from array import *

from Pieces import *
from BoardState import *

global currentPlayerColor, currentSelectedTile, currentPossibleMoves



board = BoardState()
window = tk.Tk()


#create all the pawns
boardI = 0
while (boardI < 8):
    pawn = Pawn(boardI, 1, "black", tk.PhotoImage(file = "images/Pawn_Black.png"))
    board.board[boardI][1].setCurrentPiece(pawn)
    boardI = boardI + 1

boardI = 0
while (boardI < 8):
    pawn = Pawn(boardI, 6, "white", tk.PhotoImage(file = "images/Pawn_White.png"))
    board.board[boardI][6].setCurrentPiece(pawn)
    boardI = boardI + 1
#create all the Rooks
board.board[0][0].setCurrentPiece(Rook(0,0,"black", tk.PhotoImage(file = "images/Rook_Black.png")))
board.board[7][0].setCurrentPiece(Rook(7,0,"black", tk.PhotoImage(file = "images/Rook_Black.png")))
board.board[0][7].setCurrentPiece(Rook(0,7,"white", tk.PhotoImage(file = "images/Rook_White.png")))
board.board[7][7].setCurrentPiece(Rook(7,7,"white", tk.PhotoImage(file = "images/Rook_White.png")))
#Create all the Knights
board.board[1][0].setCurrentPiece(Knight(1,0,"black", tk.PhotoImage(file = "images/Knight_Black.png")))
board.board[6][0].setCurrentPiece(Knight(6,0,"black", tk.PhotoImage(file = "images/Knight_Black.png")))
board.board[1][7].setCurrentPiece(Knight(1,7,"white", tk.PhotoImage(file = "images/Knight_White.png")))
board.board[6][7].setCurrentPiece(Knight(6,7,"white", tk.PhotoImage(file = "images/Knight_White.png")))
#Create all the Bishops
board.board[2][0].setCurrentPiece(Bishop(2,0,"black", tk.PhotoImage(file = "images/Bishop_Black.png")))
board.board[5][0].setCurrentPiece(Bishop(5,0,"black", tk.PhotoImage(file = "images/Bishop_Black.png")))
board.board[2][7].setCurrentPiece(Bishop(2,7,"white", tk.PhotoImage(file = "images/Bishop_White.png")))
board.board[5][7].setCurrentPiece(Bishop(5,7,"white", tk.PhotoImage(file = "images/Bishop_White.png")))
#Create the Queens
board.board[3][0].setCurrentPiece(Queen(3,0,"black", tk.PhotoImage(file = "images/Queen_Black.png")))
board.board[3][7].setCurrentPiece(Queen(3,7,"white", tk.PhotoImage(file = "images/Queen_White.png")))
#Create the Kings
board.board[4][0].setCurrentPiece(King(4,0,"black", tk.PhotoImage(file = "images/King_Black.png")))
board.board[4][7].setCurrentPiece(King(4,7,"white", tk.PhotoImage(file = "images/King_White.png")))


canvas = tk.Canvas(window, bg="white", width=810, height=810)

currentColPos = 10
currentRowPos = 0

for r in board.board:
    for c in r:
        coord = currentColPos, currentRowPos, currentColPos + 100, currentRowPos, currentColPos + 100, currentRowPos + 100, currentColPos, currentRowPos + 100
        box = canvas.create_polygon(coord, fill = c.color)
        if(c.piece):
            image = canvas.create_image(currentColPos, currentRowPos, anchor = tk.NW, image = c.piece.image)
        currentRowPos += 100
    #currentColPos = 10
    currentRowPos = 0
    currentColPos +=100

currentPlayerColor = "white"
currentSelectedTile = []
currentPossibleMoves = []

def buttonPressed(event):

    global currentPlayerColor, currentSelectedTile, currentPossibleMoves
    canvas.focus_set()
    if(event.x < 10 or event.y < 0 or event.y > 800 or event.x > 800):
        return
    tileX = int((event.x - 10) / 100)
    tileY = int(event.y / 100)
    print(tileX, ",", tileY)
    if board.board[tileX][tileY].hasPiece():
        #print(board.board[tileX][tileY].piece.x, ",", board.board[tileX][tileY].piece.y)
        print(board.board[tileX][tileY].piece.getAvailableMoves(board))


canvas.bind("<Button-1>", buttonPressed)
canvas.pack()





window.mainloop()
