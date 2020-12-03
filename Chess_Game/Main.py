import tkinter as tk
import numpy as np
import math
import copy
from array import *

from Pieces import *
from BoardState import *



global currentPlayerColor, currentPieceSelected, currentPossibleMoves



MAX_DEPTH = 2

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

#color - color of the player to evaluate in relation to (color of whatever player the AI is)
#tree - the state tree to evaluate (pass the root node of the current board)
#minmax - whether the current node is a min or a max (should be max)
def abMinMax(color, tree, minmax):
    if(len(tree.children) == 0):
        tree.eval = tree.state.evaluate(color)
        return tree
    else:
        evaluation = None
        for i in tree.children:
            if minmax == 'min':
                value = abMinMax(color, i, 'max')
                if evaluation is None or value.eval < evaluation.eval:
                    evaluation = value
            else:
                value = abMinMax(color, i, 'min')
                if evaluation is None or value.eval > evaluation.eval:
                    evaluation = value
        tree.eval = evaluation.eval
        if tree.parent == None:
            return evaluation
        else:
            return tree


#create the board and window
board = BoardState()
window = tk.Tk()
imageFiles = [tk.PhotoImage(file = 'images/Pawn_Black.png'),
              tk.PhotoImage(file = 'images/Rook_Black.png'),
              tk.PhotoImage(file = 'images/Knight_Black.png'),
              tk.PhotoImage(file = 'images/Bishop_Black.png'),
              tk.PhotoImage(file = 'images/Queen_Black.png'),
              tk.PhotoImage(file = 'images/King_Black.png'),
              tk.PhotoImage(file = 'images/Pawn_White.png'),
              tk.PhotoImage(file = 'images/Rook_White.png'),
              tk.PhotoImage(file = 'images/Knight_White.png'),
              tk.PhotoImage(file = 'images/Bishop_White.png'),
              tk.PhotoImage(file = 'images/Queen_White.png'),
              tk.PhotoImage(file = 'images/King_White.png')]


#create all the pawns
for i in range(8):
    board.addPiece(Pawn(i,1,'black',PAWN_BLACK))

for i in range(8):
    board.addPiece(Pawn(i,6,'white',PAWN_WHITE))
#create all the Rooks
board.addPiece(Rook(0,0,'black', ROOK_BLACK))
board.addPiece(Rook(7,0,'black', ROOK_BLACK))
board.addPiece(Rook(0,7,'white', ROOK_WHITE))
board.addPiece(Rook(7,7,'white', ROOK_WHITE))
#Create all the Knights
board.addPiece(Knight(1,0,'black', KNIGHT_BLACK))
board.addPiece(Knight(6,0,'black', KNIGHT_BLACK))
board.addPiece(Knight(1,7,'white', KNIGHT_WHITE))
board.addPiece(Knight(6,7,'white', KNIGHT_WHITE))
#Create all the Bishops
board.addPiece(Bishop(2,0,'black', BISHOP_BLACK))
board.addPiece(Bishop(5,0,'black', BISHOP_BLACK))
board.addPiece(Bishop(2,7,'white', BISHOP_WHITE))
board.addPiece(Bishop(5,7,'white', BISHOP_WHITE))
#Create the Queens
board.addPiece(Queen(3,0,'black', QUEEN_BLACK))
board.addPiece(Queen(3,7,'white', QUEEN_WHITE))
#Create the Kings
board.addPiece(King(4,0,'black', KING_BLACK))
board.addPiece(King(4,7,'white', KING_WHITE))

print("Board Evaluation (White):", board.evaluate("white"))
print("Board Evaluation (Black):", board.evaluate("black"))
print()
#tree = board.createTree('white')
#newBoard = abMinMax('white', tree, 'max')

canvas = tk.Canvas(window, bg='white', width=800, height=800)

#holds all the polygons so they can be redrawn later
matrix = np.zeros((8, 8))
#holds all the images so they can be redrawn later
images = []

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
        matrix[col_index, row_index] = box

for i in board.blackPieces:
    image_id = canvas.create_image(i.x * 100, i.y * 100, anchor = tk.NW, image = imageFiles[i.image])
    i.canvas_image = image_id
for i in board.whitePieces:
    image_id = canvas.create_image(i.x * 100, i.y * 100, anchor=tk.NW, image = imageFiles[i.image])
    i.canvas_image = image_id

currentPlayerColor = 'white'
currentPieceSelected = []
currentPossibleMoves = []
changed_tiles = []
matrix_int = matrix.astype(np.int)  # Convert Matrix from float 64 to int so item config can be used


def buttonPressed(event):
    global currentPlayerColor, currentPieceSelected, currentPossibleMoves, changed_tiles
    canvas.focus_set()
    if(event.x < 10 or event.y < 0 or event.y > 800 or event.x > 800):
        return

    tileX = int(event.x / 100)
    tileY = int(event.y / 100)
    print(tileX, ",", tileY)
    current_piece = board.getPieceAt(tileX, tileY)
    # If the color of a tile was changed previously, revert back to original
    if changed_tiles:
        for item_tuple in changed_tiles:
            canvas.itemconfig(item_tuple[0], fill=item_tuple[1], outline="")
        coordX = math.floor(event.x / 100) * 100
        coordY = math.floor(event.y / 100) * 100
        current_piece = board.getPieceAt(tileX, tileY)

        # If the current possible move is clicked on moved the piece
        if [tileX, tileY] in currentPossibleMoves:
            previous_piece = currentPieceSelected
            # Only on the players turn can they move a piece
            if previous_piece.color == currentPlayerColor:
                canvas_image = previous_piece.canvas_image
                image = imageFiles[previous_piece.image]

                if board.getPieceAt(tileX, tileY):
                    piece_to_delete = board.getPieceAt(tileX, tileY)
                    canvas.delete(piece_to_delete.canvas_image)
                    piece_to_delete.x = None
                    piece_to_delete.y = None

                canvas.delete(canvas_image)
                previous_piece.canvas_image = canvas.create_image(coordX, coordY, anchor= tk.NW, image=image)

                #Update board State
                previous_piece.x = tileX
                previous_piece.y = tileY
                previous_piece.moved = True

                # Switch colors
                if(currentPlayerColor == "white"):
                    currentPlayerColor = "black"
                elif(currentPlayerColor == "black"):
                    currentPlayerColor = "white"


        # Clear changed tiles after
        changed_tiles = []
    # If there is no current selected piece
    elif board.pieceAt(tileX, tileY) != 'none':
        available_moves = current_piece.getAvailableMoves(board)
        currentPossibleMoves = available_moves
        print(available_moves)

        # Highlight current Tile Selected
        tile_selected = matrix_int[tileX][tileY]
        color = canvas.itemcget(tile_selected, "fill")
        changed_tiles.append((tile_selected, color))
        canvas.itemconfig(tile_selected, width="5", outline="orange")

        # Turn every available move for the piece to blue with red outline
        if available_moves:
            for possible_moves_tiles in available_moves:
                x_cord = possible_moves_tiles[0]
                y_cord = possible_moves_tiles[1]

                if board.pieceAt(x_cord, y_cord) != currentPlayerColor:
                    item = matrix_int[x_cord, y_cord]
                    original_color = canvas.itemcget(item, "fill")
                    # Store the tile and the color of the coordinate so it
                    # can be reverted back later
                    changed_tiles.append((item, original_color))
                    canvas.itemconfig(item, fill = "blue", width = "5", outline = "red")
    currentPieceSelected = current_piece


canvas.bind('<Button-1>', buttonPressed)
def checkPiece(piece):
    return piece.type
canvas.bind("<Button-1>", buttonPressed)
canvas.pack()

window.mainloop()
