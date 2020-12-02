import tkinter as tk
import numpy as np
import copy
from array import *

from Pieces import *
from BoardState import *



global currentPlayerColor, currentSelectedPiece, currentPossibleMoves

MAX_DEPTH = 3

#returns the color a tile should be based on its position
def getTileColor(x,y):
    if (x % 2 == 0):
        if(y % 2 == 0):
            return 'white'
        else:
            return 'black'
    else:
        if(y % 2 == 0):
            return 'black'
        else:
            return 'white'


#create the board and window
board = BoardState()
window = tk.Tk()


#create all the pawns
for i in range(8):
    board.addPiece(Pawn(i,1,'black',tk.PhotoImage(file = 'images/Pawn_Black.png')))

for i in range(8):
    board.addPiece(Pawn(i,6,'white',tk.PhotoImage(file = 'images/Pawn_Black.png')))
#create all the Rooks
board.addPiece(Rook(0,0,'black', tk.PhotoImage(file = 'images/Rook_Black.png')))
board.addPiece(Rook(7,0,'black', tk.PhotoImage(file = 'images/Rook_Black.png')))
board.addPiece(Rook(0,7,'white', tk.PhotoImage(file = 'images/Rook_White.png')))
board.addPiece(Rook(7,7,'white', tk.PhotoImage(file = 'images/Rook_White.png')))
#Create all the Knights
board.addPiece(Knight(1,0,'black', tk.PhotoImage(file = 'images/Knight_Black.png')))
board.addPiece(Knight(6,0,'black', tk.PhotoImage(file = 'images/Knight_Black.png')))
board.addPiece(Knight(1,7,'white', tk.PhotoImage(file = 'images/Knight_White.png')))
board.addPiece(Knight(6,7,'white', tk.PhotoImage(file = 'images/Knight_White.png')))
#Create all the Bishops
board.addPiece(Bishop(2,0,'black', tk.PhotoImage(file = 'images/Bishop_Black.png')))
board.addPiece(Bishop(5,0,'black', tk.PhotoImage(file = 'images/Bishop_Black.png')))
board.addPiece(Bishop(2,7,'white', tk.PhotoImage(file = 'images/Bishop_White.png')))
board.addPiece(Bishop(5,7,'white', tk.PhotoImage(file = 'images/Bishop_White.png')))
#Create the Queens
board.addPiece(Queen(3,0,'black', tk.PhotoImage(file = 'images/Queen_Black.png')))
board.addPiece(Queen(3,7,'white', tk.PhotoImage(file = 'images/Queen_White.png')))
#Create the Kings
board.addPiece(King(4,0,'black', tk.PhotoImage(file = 'images/King_Black.png')))
board.addPiece(King(4,7,'white', tk.PhotoImage(file = 'images/King_White.png')))


canvas = tk.Canvas(window, bg='white', width=800, height=800)

#holds all the polygons so they can be redrawn later
matrix = np.zeros((8, 8))
#holds all the images so they can be redrawn later
images = []

for i in board.blackPieces:
    images.append(canvas.create_image(i.x * 100, i.y * 100, anchor = tk.NW, image = i.image))
for i in board.whitePieces:
    images.append(canvas.create_image(i.x * 100, i.y * 100, anchor = tk.NW, image = i.image))

row_index = -1
for r in range(8):
    row_index += 1
    col_index = -1
    for c in range(8):
        col_index += 1
        tx = c*100
        ty = r*100
        #set the coordinates of the four corners of the tile 
        coord = tx, ty, tx + 100, ty, tx + 100, ty + 100, tx, ty + 100
        #creates a polygon to represent a tile on the board
        box = canvas.create_polygon(coord, fill = getTileColor(r,c))
        # Stores every polygon created to make the black and white checker board based on coordinates
        matrix[row_index, col_index] = box
        #if(c.piece):
        #    image = canvas.create_image(currentColPos, currentRowPos, anchor = tk.NW, image = c.piece.image)

for i in board.blackPieces:
    images.append(canvas.create_image(i.x * 100, i.y * 100, anchor = tk.NW, image = i.image))
for i in board.whitePieces:
    images.append(canvas.create_image(i.x * 100, i.y * 100, anchor = tk.NW, image = i.image))

currentPlayerColor = 'white'
currentSelectedPiece = []
currentPossibleMoves = []
changed_tiles = []
matrix_int = matrix.astype(np.int)  # Convert Matrix from float 64 to int so item config can be used


def buttonPressed(event):
    global currentPlayerColor, currentSelectedPiece, currentPossibleMoves, changed_tiles
    canvas.focus_set()

    #check if click was inside the board area
    if(event.x < 0 or event.y < 0 or event.y > 800 or event.x > 800):
        return

    # If the color of a tile was changed previously, revert back to original
    if changed_tiles:
        for item_tuple in changed_tiles:
            canvas.itemconfig(item_tuple[0], fill=item_tuple[1], outline='')

    #get the tile coordinates of the click
    tileX = int(event.x / 100)
    tileY = int(event.y / 100)

    changed_tiles = []
    print(tileX, ',', tileY)
    if board.pieceAt(tileX, tileY) != 'none':
        #print(board.board[tileX][tileY].piece.x, ',', board.board[tileX][tileY].piece.y)
        available_moves = board.getPieceAt(tileX, tileY).getAvailableMoves(board)
        print(available_moves)

        # Turn every available move for the piece to blue with red outline
        if available_moves:
            for possible_moves_tiles in available_moves:
                x_cord = possible_moves_tiles[1]
                y_cord = possible_moves_tiles[0]

                item = matrix_int[x_cord, y_cord]
                original_color = canvas.itemcget(item, 'fill')
                # Store the tile and the color of the coordinate so it
                # can be reverted back later
                changed_tiles.append((item, original_color))
                canvas.itemconfig(item, fill = 'blue', width = '2', outline = 'red')


canvas.bind('<Button-1>', buttonPressed)
canvas.pack()

window.mainloop()
