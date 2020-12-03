from BoardState import *

def inBounds(x,y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

PAWN_BLACK = 0
ROOK_BLACK = 1
KNIGHT_BLACK = 2
BISHOP_BLACK = 3
QUEEN_BLACK = 4
KING_BLACK = 5
PAWN_WHITE = 6
ROOK_WHITE = 7
KNIGHT_WHITE = 8
BISHOP_WHITE = 9
QUEEN_WHITE = 10
KING_WHITE = 11

class Piece:
    def __init__(self, X, Y, Color, Image):
        self.x = X
        self.y = Y
        self.color = Color
        self.moved = False
        self.image = Image
        self.canvas_image = 0

    def getAvailableMoves(self):
        pass

    def getPointTable(self):
        pass


class Pawn(Piece):
    value = 100

    value = 1

    def __str__(self):
        return '[PAWN,' + self.color + ',' + str(self.x) + ',' + str(self.y) + ']'
    def __repr__(self):
        return '[PAWN,' + self.color + ',' + str(self.moved) + ',' + str(self.x) + ',' + str(self.y) + ']'

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
            if inBounds(self.x+1, self.y+1) and board.pieceAt(self.x+1, self.y+1) == 'white':
                toReturn.append([self.x+1, self.y+1])
            if inBounds(self.x-1, self.y+1) and board.pieceAt(self.x-1, self.y+1) == 'white':
                toReturn.append([self.x-1, self.y+1])
        return toReturn

    # Assumes that player is at bottom half (Encourage Forward Movement)
    def getPointTable(self):
        pawn_table = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [50, 50, 50, 50, 50, 50, 50, 50],
            [10, 10, 20, 30, 30, 20, 10, 10],
            [5, 5, 10, 25, 25, 10, 5, 5],
            [0, 0, 0, 20, 20, 0, 0, 0],
            [5, -5, -10, 0, 0, -10, -5, 5],
            [5, 10, 10, -20, -20, 10, 10, 5],
            [0, 0, 0, 0, 0, 0, 0, 0]]
        return pawn_table


class Rook(Piece):
    value = 550

    def getAvailableMoves(self, board):
        toReturn = []

        # check every tile along y-positive until you either reach the end or find a piece
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

    # Assumes that player is at bottom half (Encourage Rook to reach other half of board and stay away from edges)
    def getPointTable(self):
        knight_table = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [5, 10, 10, 10, 10, 10, 10,  5],
            [-5, 0,  0,  0,  0,  0,  0, -5],
            [-5, 0,  0,  0,  0,  0,  0, -5],
            [-5, 0,  0,  0,  0,  0,  0, -5],
            [-5, 0,  0,  0,  0,  0,  0, -5],
            [-5, 0,  0,  0,  0,  0,  0, -5],
            [0, 0, 0, 5, 5, 0, 0]]
        return knight_table


class Knight(Piece):
    value = 300

    def __str__(self):
        return '[KNIGHT,' + self.color + ',' + str(self.x) + ',' + str(self.y) + ']'
    def __repr__(self):
        return '[KNIGHT,' + self.color + ',' + str(self.moved) + ',' + str(self.x) + ',' + str(self.y) + ']'

    def getAvailableMoves(self, board):
        toReturn = []
        possibleMoves = [[self.x - 1, self.y - 2],
                         [self.x + 1, self.y - 2],
                         [self.x - 2, self.y - 1],
                         [self.x + 2, self.y - 1],
                         [self.x - 2, self.y + 1],
                         [self.x + 2, self.y + 1],
                         [self.x - 1, self.y + 2],
                         [self.x + 1, self.y + 2]]

        for i in possibleMoves:
            if inBounds(i[0],i[1]):
                piece = board.pieceAt(i[0],i[1])
                if piece != 'none':
                    if piece != self.color:
                        toReturn.append([i[0],i[1]])
                else:
                    toReturn.append([i[0],i[1]])
        return toReturn

    # Assumes that player is at bottom half (Encourage Rook to reach other half of board and stay away from edges)
    def getPointTable(self):
        rook_table = [
            [-50,-40,-30,-30,-30,-30,-40,-50],
            [-40,-20,  0,  0,  0,  0,-20,-40],
            [-30,  0, 10, 15, 15, 10,  0,-30],
            [30,  5, 15, 20, 20, 15,  5,-30],
            [-30,  0, 15, 20, 20, 15,  0,-30],
            [-30,  5, 10, 15, 15, 10,  5,-30],
            [-40,-20,  0,  5,  5,  0,-20,-40],
            [-50,-40,-30,-30,-30,-30,-40,-50]]
        return rook_table


class Bishop(Piece):
    value = 350
    def __str__(self):
        return '[BISHOP,' + self.color + ',' + str(self.x) + ',' + str(self.y) + ']'
    def __repr__(self):
        return '[BISHOP,' + self.color + ',' + str(self.moved) + ',' + str(self.x) + ',' + str(self.y) + ']'

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
    value = 1000
    def __str__(self):
        return '[QUEEN,' + self.color + ',' + str(self.x) + ',' + str(self.y) + ']'
    def __repr__(self):
        return '[QUEEN,' + self.color + ',' + str(self.moved) + ',' + str(self.x) + ',' + str(self.y) + ']'

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

    def __str__(self):
        return '[KING,' + self.color + ',' + str(self.x) + ',' + str(self.y) + ']'
    def __repr__(self):
        return '[KING,' + self.color + ',' + str(self.moved) + ',' + str(self.x) + ',' + str(self.y) + ']'

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
