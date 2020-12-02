import math
import tkinter as tk
import numpy as np
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

matrix = np.zeros((8, 8))
row_index = -1
for r in board.board:
    row_index += 1
    col_index = -1
    for c in r:
        col_index += 1
        coord = currentColPos, currentRowPos, currentColPos + 100, currentRowPos, currentColPos + 100, currentRowPos + 100, currentColPos, currentRowPos + 100
        box = canvas.create_polygon(coord, fill = c.color)
        # Stores every polygon created to make the black and white checker board based on coordinates
        matrix[row_index, col_index] = box
        if(c.piece):
            c.piece.canvas_image = canvas.create_image(currentColPos, currentRowPos, anchor = tk.NW, image = c.piece.image)
        currentRowPos += 100
    # currentColPos = 10
    currentRowPos = 0
    currentColPos += 100

currentPlayerColor = "white"
currentSelectedTile = []
currentPossibleMoves = []
changed_tiles = []
currentPlayerColor = "white"
matrix_int = matrix.astype(np.int)  # Convert Matrix from float 64 to int so item config can be used


def buttonPressed(event):
    global currentPlayerColor, currentSelectedTile, currentPossibleMoves, changed_tiles
    canvas.focus_set()
    if(event.x < 10 or event.y < 0 or event.y > 800 or event.x > 800):
        return

    tileX = int((event.x - 10) / 100)
    tileY = int(event.y / 100)
    print(tileX, ",", tileY)

    # If the color of a tile was changed previously, revert back to original
    if changed_tiles:
        for item_tuple in changed_tiles:
            canvas.itemconfig(item_tuple[0], fill=item_tuple[1], outline="")
        coordX = math.floor(event.x / 100) * 100 + 10
        coordY = math.floor(event.y / 100) * 100

        # If the current possible move is clicked on moved the piece
        if [tileX, tileY] in currentPossibleMoves:
            current_piece = currentSelectedTile.piece
            # Only on the players turn can they move a piece
            if current_piece.color == currentPlayerColor:
                canvas_image = current_piece.canvas_image
                image = currentSelectedTile.piece.image
                canvas.delete(canvas_image)
                currentSelectedTile.piece.canvas_image = canvas.create_image(coordX, coordY, anchor= tk.NW, image=image)

                #Update board State
                board.board[current_piece.x][current_piece.y].piece = None
                board.board[tileX][tileY].piece = current_piece
                current_piece.x = tileX
                current_piece.y = tileY

                # Switch colors
                if(currentPlayerColor == "white"):
                    currentPlayerColor = "black"
                elif(currentPlayerColor == "black"):
                    currentPlayerColor = "white"


        # Clear changed tiles after
        changed_tiles = []
    # If there is no current selected piece
    elif board.board[tileX][tileY].hasPiece():
        # print(board.board[tileX][tileY].piece.x, ",", board.board[tileX][tileY].piece.y)
        available_moves = board.board[tileX][tileY].piece.getAvailableMoves(board)
        currentPossibleMoves = available_moves
        print(available_moves)

        # Turn every available move for the piece to blue with red outline
        if available_moves:
            for possible_moves_tiles in available_moves:
                x_cord = possible_moves_tiles[0]
                y_cord = possible_moves_tiles[1]

                item = matrix_int[x_cord, y_cord]
                original_color = canvas.itemcget(item, "fill")
                # Store the tile and the color of the coordinate so it
                # can be reverted back later
                changed_tiles.append((item, original_color))
                canvas.itemconfig(item, fill = "blue", width = "10", outline = "red")
    currentSelectedTile = board.board[tileX][tileY]


def checkPiece(piece):
    return piece.type
canvas.bind("<Button-1>", buttonPressed)
canvas.pack()

window.mainloop()
