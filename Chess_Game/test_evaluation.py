from Pieces import *
from BoardState import *
from Main import *


rookTakesQueen = BoardState()

rookTakesQueen.addPiece(Pawn(4,3,'black',PAWN_BLACK))
rookTakesQueen.addPiece(Pawn(3,4,'white',PAWN_WHITE))
rookTakesQueen.addPiece(Rook(5,6,'white', ROOK_WHITE))
rookTakesQueen.addPiece(Queen(5,1,'black', QUEEN_BLACK))


itsBaitMate = BoardState()

itsBaitMate.addPiece(Queen(1,3,'black', QUEEN_BLACK))
itsBaitMate.addPiece(Knight(3,3,'white', KNIGHT_WHITE))
itsBaitMate.addPiece(Rook(3,6,'white', ROOK_WHITE))


doYourJob = BoardState()

doYourJob.addPiece(Queen(3,2,'black', QUEEN_BLACK))
doYourJob.addPiece(Knight(3,6,'white', KNIGHT_WHITE))
doYourJob.addPiece(Rook(5,5,'black', ROOK_BLACK))
doYourJob.addPiece(King(3,7,'white', KING_WHITE))

you_might_outnumbered = BoardState()

you_might_outnumbered.addPiece()

print("Rook Takes Queen", rookTakesQueen)
print(rookTakesQueen.evaluate('black'))
print(rookTakesQueen.evaluate('white'))

print(abMinMax('white', rookTakesQueen.createTree('white'), 'max').state)
print('\n')

print("Its Bait Mate", itsBaitMate)
print(itsBaitMate.evaluate('black'))
print(itsBaitMate.evaluate('white'))

print(abMinMax('black', itsBaitMate.createTree('black'), 'max').state)
print('\n')

print("Do Your Job", doYourJob)
print(doYourJob.evaluate('black'))
print(doYourJob.evaluate('white'))

print(abMinMax('white', doYourJob.createTree('white'), 'max').state)
print('\n')