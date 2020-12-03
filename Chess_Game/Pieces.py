from BoardState import *

def inBounds(x,y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

class Piece:
    def __init__(self, X, Y, Color, Image):
        self.x = X
        self.y = Y
        self.color = Color
        self.value = 0
        self.moved = False
        self.image = Image
        self.canvas_image = 0;

    def getAvailableMoves(self):
        pass
class Pawn(Piece):
    value = 1
    def getAvailableMoves(self, board):
        toReturn = []
        if self.color == 'white':
            if inBounds(self.x, self.y-1) and board.pieceAt(self.x, self.y-1) == 'none':
                toReturn.append([self.x, self.y-1])
                if not self.moved:
                    if board.pieceAt(self.x, self.y-2) == 'none':
                        toReturn.append([self.x, self.y-2])
            if inBounds(self.x+1, self.y-1) and board.pieceAt(self.x+1, self.y-1) == 'black':
                toReturn.append([self.x+1, self.y-1])
            if inBounds(self.x-1, self.y-1) and board.pieceAt(self.x-1, self.y-1) == 'black':
                toReturn.append([self.x-1, self.y-1])
        else:

            if inBounds(self.x, self.y+1) and board.pieceAt(self.x, self.y+1) == 'none':
                toReturn.append([self.x, self.y+1])
                if not self.moved:
                    if board.pieceAt(self.x, self.y+2) == 'none':
                        toReturn.append([self.x, self.y+2])
            if inBounds(self.x+1, self.y+1) and board.pieceAt(self.x+1, self.y+1) == 'black':
                toReturn.append([self.x+1, self.y+1])
            if inBounds(self.x-1, self.y+1) and board.pieceAt(self.x-1, self.y+1) == 'black':
                toReturn.append([self.x-1, self.y+1])
        return toReturn

class Rook(Piece):
    value = 5
    def getAvailableMoves(self, board):
        toReturn = []

        #check every tile along y-positive until you either reach the end or find a piece
        X = self.x
        Y = self.y+1
        while(Y < 8):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y+1
        #check every tile along y-negative until you either reach the end or find a piece
        X = self.x
        Y = self.y-1
        while(Y >= 0):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y-1
        #check every tile along x-positive until you either reach the end or find a piece
        X = self.x+1
        Y = self.y
        while(X < 8):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X+1
        #check every tile along x-negative until you either reach the end or find a piece
        X = self.x-1
        Y = self.y
        while(X >= 0):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1

        return toReturn

class Knight(Piece):
    value = 5
    def getAvailableMoves(self, board):
        toReturn = []
        possibleMoves = [[self.x-1, self.y-2],
                         [self.x+1, self.y-2],
                         [self.x-2, self.y-1],
                         [self.x+2, self.y-1],
                         [self.x-2, self.y+1],
                         [self.x+2, self.y+1],
                         [self.x-1, self.y+2],
                         [self.x+1, self.y+2]]

        for i in possibleMoves:
            if inBounds(i[0],i[1]):
                piece = board.pieceAt(i[0],i[1])
                if piece != 'none':
                    if piece != self.color:
                        toReturn.append([i[0],i[1]])
                else:
                    toReturn.append([i[0],i[1]])
        return toReturn


class Bishop(Piece):
    value = 5
    def getAvailableMoves(self, board):
        toReturn = []

        #check every tile along x-positive y-positive until you either reach the end or find a piece
        X = self.x+1
        Y = self.y+1
        while(Y < 8 and X < 8):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y+1
            X = X+1
        #check every tile along x-positive y-negative until you either reach the end or find a piece
        X = self.x+1
        Y = self.y-1
        while(Y >= 0 and X < 8):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y-1
            X = X+1
        #check every tile along x-negative y-positive until you either reach the end or find a piece
        X = self.x-1
        Y = self.y+1
        while(X >= 0 and Y < 8):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1
            Y = Y+1
        #check every tile along x-negative y-negative until you either reach the end or find a piece
        X = self.x-1
        Y = self.y-1
        while(X >= 0 and Y >= 0):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1
            Y = Y-1

        return toReturn

class Queen(Piece):
    value = 5
    def getAvailableMoves(self, board):
        toReturn = []

        #check every tile along y-positive until you either reach the end or find a piece
        X = self.x
        Y = self.y+1
        while(Y < 8):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y+1
        #check every tile along y-negative until you either reach the end or find a piece
        X = self.x
        Y = self.y-1
        while(Y >= 0):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y-1
        #check every tile along x-positive until you either reach the end or find a piece
        X = self.x+1
        Y = self.y
        while(X < 8):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X+1
        #check every tile along x-negative until you either reach the end or find a piece
        X = self.x-1
        Y = self.y
        while(X >= 0):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1
        #check every tile along x-positive y-positive until you either reach the end or find a piece
        X = self.x+1
        Y = self.y+1
        while(Y < 8 and X < 8):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y+1
            X = X+1
        #check every tile along x-positive y-negative until you either reach the end or find a piece
        X = self.x+1
        Y = self.y-1
        while(Y >= 0 and X < 8):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y-1
            X = X+1
        #check every tile along x-negative y-positive until you either reach the end or find a piece
        X = self.x-1
        Y = self.y+1
        while(X >= 0 and Y < 8):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1
            Y = Y+1
        #check every tile along x-negative y-negative until you either reach the end or find a piece
        X = self.x-1
        Y = self.y-1
        while(X >= 0 and Y >= 0):
            piece = board.pieceAt(X,Y)
            if piece != 'none':
                if piece != self.color:
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1
            Y = Y-1
        return toReturn

class King(Piece):
    value = 10000000
    def getAvailableMoves(self, board):
        toReturn = []
        possibleMoves = [[self.x-1, self.y-1],
                         [self.x-1, self.y],
                         [self.x-1, self.y+1],
                         [self.x, self.y-1],
                         [self.x, self.y+1],
                         [self.x+1, self.y-1],
                         [self.x+1, self.y],
                         [self.x+1, self.y+1]]

        for i in possibleMoves:
            if inBounds(i[0],i[1]):
                piece = board.pieceAt(i[0],i[1])
                if piece != 'none':
                    if piece != self.color:
                        toReturn.append([i[0],i[1]])
                else:
                    toReturn.append([i[0],i[1]])

        return toReturn
