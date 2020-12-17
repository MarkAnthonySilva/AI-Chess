
from Pieces import *
from BoardState import *
from Main import *
import time

singlePawnBoard = BoardState()

singlePawnBoard.addPiece(Pawn(3, 3, 'white', PAWN_WHITE))

rookTakesQueen = BoardState()

rookTakesQueen.addPiece(Pawn(4,3,'black',PAWN_BLACK))
rookTakesQueen.addPiece(Pawn(3,4,'white',PAWN_WHITE))
rookTakesQueen.addPiece(Rook(5,6,'white', ROOK_WHITE))
rookTakesQueen.addPiece(Queen(5,1,'black', QUEEN_BLACK))

for i in rookTakesQueen.blackPieces:
    i.moved = True
for i in rookTakesQueen.whitePieces:
    i.moved = True

itsBaitMate = BoardState()

itsBaitMate.addPiece(Queen(1,3,'black', QUEEN_BLACK))
itsBaitMate.addPiece(Knight(3,3,'white', KNIGHT_WHITE))
itsBaitMate.addPiece(Rook(3,6,'white', ROOK_WHITE))

for i in itsBaitMate.blackPieces:
    i.moved = True
for i in itsBaitMate.whitePieces:
    i.moved = True

doYourJob = BoardState()

doYourJob.addPiece(Queen(3,2,'black', QUEEN_BLACK))
doYourJob.addPiece(Knight(3,6,'white', KNIGHT_WHITE))
doYourJob.addPiece(Rook(5,5,'black', ROOK_BLACK))
doYourJob.addPiece(King(3,7,'white', KING_WHITE))

for i in doYourJob.blackPieces:
    i.moved = True
for i in doYourJob.whitePieces:
    i.moved = True

you_might_be_outnumbered = BoardState()

# you_might_be_outnumbered.addPiece()
print("Capital Letter: Black, Lower Case: White")
print("Single Pawn Board", singlePawnBoard)
print("White Score:", singlePawnBoard.evaluate('white'))
print()

print("Rook Takes Queen: Before State", rookTakesQueen)
print("Black Score:", rookTakesQueen.evaluate('black'))
print("White Score:", rookTakesQueen.evaluate('white'))

start = time.time()
tree_state = abMax('white', rookTakesQueen, math.inf, 0)
end = time.time()
print("Rook Takes Queen: After State", tree_state)
print("Black Score:", tree_state.evaluate('black'))
print("White Score:", tree_state.evaluate('white'))
print("time taken: ", end - start)
print('\n')

print("Its Bait Mate", itsBaitMate)
print("Black Score:",itsBaitMate.evaluate('black'))
print("White Score:", itsBaitMate.evaluate('white'))
start = time.time()
print("Its Bait Mate: After State", abMax('black', itsBaitMate, math.inf, 0))
end = time.time()
print("Black Score:", tree_state.evaluate('black'))
print("White Score:", tree_state.evaluate('white'))
print("time taken: ", end - start)
print('\n')

print("Do Your Job", doYourJob)
print("Black Score:",doYourJob.evaluate('black'))
print("White Score:", doYourJob.evaluate('white'))

start = time.time()
print("Do Your Job: After State", abMax('white', doYourJob, math.inf, 0))
end = time.time()
print("Black Score:", tree_state.evaluate('black'))
print("White Score:", tree_state.evaluate('white'))
print("time taken: ", end - start)
print('\n')
