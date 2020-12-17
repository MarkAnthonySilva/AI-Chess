import tkinter as tk
import numpy as np
import math
import copy
from array import *

from Pieces import *
from BoardState import *



global currentPlayerColor, currentPieceSelected, currentPossibleMoves, changed_tiles, matrix_int



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

def reverse(str):
    if str == 'white':
        return 'black'
    else:
        return 'white'


def abMax(color:str, state:BoardState, pruningValue:int, depth:int):
    #if this is a leaf node, return the evaluation of the state
    if(depth >= MAX_DEPTH):
        return state.evaluate(color)
    else:
        pieces = state.getColorPieces(color)
        bestState = None
        bestEval = -math.inf
        #for every possible move
        for i in pieces:
            moves = i.getAvailableMoves(state)
            for j in moves:
                #create a new state from that move
                newState = state.stateAfterMove(i.x, i.y, j[0], j[1])
                #evaluate that state, using the current best as the pruning value
                eval = abMin(color, newState, bestEval, depth + 1)
                #if the evaluation is greater than the pruning value, stop evaluating this node
                if eval > pruningValue:
                    return math.inf
                #if the evaluation is higher than the current highest, save this evaluation
                if eval > bestEval:
                    bestEval = eval
                    bestState = newState
        #if this is the root node, return the chosen state, otherwise return the best evaluation
        if depth == 0:
            return bestState
        else:
            return bestEval

def abMin(color:str, state:BoardState, pruningValue:int, depth:int):
    if(depth >= MAX_DEPTH):
        return state.evaluate(color)
    else:
        pieces = state.getColorPieces(color)
        bestState = None
        bestEval = math.inf
        #for every possible move
        for i in pieces:
            moves = i.getAvailableMoves(state)
            for j in moves:
                #create a new state from that move
                newState = state.stateAfterMove(i.x, i.y, j[0], j[1])
                #evaluate that state, using the current best as the pruning value
                eval = abMax(color, newState, bestEval, depth + 1)
                #if the evaluation is less than the pruning value, stop evaluating this node
                if eval < pruningValue:
                    return -math.inf
                #if the evaluation is lower than the current lowest, save this evaluation
                if eval < bestEval:
                    bestEval = eval
                    bestState = newState
        #if this is the root node, return the chosen state, otherwise return the best evaluation
        if depth == 0:
            return bestState
        else:
            return bestEval





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
board.blackKing = board.blackPieces[len(board.blackPieces)-1]
board.addPiece(King(4,7,'white', KING_WHITE))
board.whiteKing = board.whitePieces[len(board.whitePieces)-1]

print("Board Evaluation (White):", board.evaluate("white"))
print("Board Evaluation (Black):", board.evaluate("black"))
print()

#AI will be white, have it make the first move
board = abMax('white', board, math.inf, 0)

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

currentPlayerColor = 'black'
currentPieceSelected = []
currentPossibleMoves = []
changed_tiles = []
matrix_int = matrix.astype(np.int)  # Convert Matrix from float 64 to int so item config can be used

print(canvas.find_all())


def buttonPressed(event):
    global currentPlayerColor, currentPieceSelected, currentPossibleMoves, changed_tiles, matrix_int, board, canvas
    if not board.inCheckMate('white') and not board.inCheckMate('black'):
        
        canvas.focus_set()
        if(event.x < 10 or event.y < 0 or event.y > 800 or event.x > 800):
            return

        tileX = int(event.x / 100)
        tileY = int(event.y / 100)

        print('[',tileX, ",", tileY,']', board.getPieceAt(tileX, tileY))

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
                    #update the board state
                    board = board.stateAfterMove(previous_piece.x, previous_piece.y, tileX, tileY)
                    #get the list of all canvas objects and a list of all canvas images
                    canvas_objects = canvas.find_all()
                    board_objects = []
                    for i in board.blackPieces:
                        board_objects.append(i.canvas_image)
                        canvas.coords(i.canvas_image, i.x * 100, i.y * 100)
                    for i in board.whitePieces:
                        board_objects.append(i.canvas_image)
                        canvas.coords(i.canvas_image, i.x * 100, i.y * 100)

                    for i in canvas_objects:
                        if i not in board_objects and i > 64:
                            canvas.delete(i)

                    # Switch colors
                    board = abMax('white', board, math.inf, 0)
                    canvas_objects = canvas.find_all()
                    board_objects = []
                    for i in board.blackPieces:
                        board_objects.append(i.canvas_image)
                        canvas.coords(i.canvas_image, i.x * 100, i.y * 100)
                    for i in board.whitePieces:
                        board_objects.append(i.canvas_image)
                        canvas.coords(i.canvas_image, i.x * 100, i.y * 100)

                    for i in canvas_objects:
                        if i not in board_objects and i > 64:
                            canvas.delete(i)

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