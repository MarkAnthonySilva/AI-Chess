from BoardState import *

def inBounds(x,y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

class Piece:
    def __init__(self, X, Y, Color, Image):
        self.x = X
        self.y = Y
        self.color = Color
        self.value = 0
        self.image = Image

    def getAvailableMoves(self):
        pass

class Pawn(Piece):
    value = 1
    moved = False
    def getAvailableMoves(self, board):
        toReturn = []
        if self.color == "white":
            if not self.moved:
                if not board.board[self.x][self.y-2].hasPiece():
                    toReturn.append([self.x, self.y-2])
            if inBounds(self.x, self.y-1) and not board.board[self.x][self.y-1].hasPiece():
                    toReturn.append([self.x, self.y-1])
            if inBounds(self.x+1, self.y-1) and board.board[self.x+1][self.y-1].hasEnemyPiece(self.color):
                   toReturn.append([self.x+1, self.y-1])
            if inBounds(self.x-1, self.y-1) and board.board[self.x-1][self.y-1].hasEnemyPiece(self.color):
                   toReturn.append([self.x-1, self.y-1])
        else:
            if not self.moved:
                if not board.board[self.x][self.y+2].hasPiece():
                    toReturn.append([self.x, self.y+2])
            if inBounds(self.x, self.y+1) and not board.board[self.x][self.y+1].hasPiece():
                    toReturn.append([self.x, self.y+1])
            if inBounds(self.x+1, self.y+1) and board.board[self.x+1][self.y+1].hasEnemyPiece(self.color):
                   toReturn.append([self.x+1, self.y+1])
            if inBounds(self.x-1, self.y+1) and board.board[self.x-1][self.y+1].hasEnemyPiece(self.color):
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
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y+1
        #check every tile along y-negative until you either reach the end or find a piece
        X = self.x
        Y = self.y-1
        while(Y >= 0):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y-1
        #check every tile along x-positive until you either reach the end or find a piece
        X = self.x+1
        Y = self.y
        while(X < 8):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X+1
        #check every tile along x-negative until you either reach the end or find a piece
        X = self.x-1
        Y = self.y
        while(X >= 0):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1

        return toReturn

class Knight(Piece):
    value = 5
    def getAvailableMoves(self, board):
        toReturn = []

        X = self.x-1
        Y = self.y-2
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x+1
        Y = self.y-2
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x-2
        Y = self.y-1
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x+2
        Y = self.y-1
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x-2
        Y = self.y+1
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x+2
        Y = self.y+1
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x-1
        Y = self.y+2
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x-1
        Y = self.y+2
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        return toReturn


class Bishop(Piece):
    value = 5
    def getAvailableMoves(self, board):
        toReturn = []

        #check every tile along x-positive y-positive until you either reach the end or find a piece
        X = self.x+1
        Y = self.y+1
        while(Y < 8 and X < 8):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y+1
            X = X+1
        #check every tile along x-positive y-negative until you either reach the end or find a piece
        X = self.x+1
        Y = self.y-1
        while(Y >= 0 and X < 8):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y-1
            X = X+1
        #check every tile along x-negative y-positive until you either reach the end or find a piece
        X = self.x-1
        Y = self.y+1
        while(X >= 0 and Y < 8):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1
            Y = Y+1
        #check every tile along x-negative y-negative until you either reach the end or find a piece
        X = self.x-1
        Y = self.y-1
        while(X >= 0 and Y >= 0):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
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
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y+1
        #check every tile along y-negative until you either reach the end or find a piece
        X = self.x
        Y = self.y-1
        while(Y >= 0):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y-1
        #check every tile along x-positive until you either reach the end or find a piece
        X = self.x+1
        Y = self.y
        while(X < 8):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X+1
        #check every tile along x-negative until you either reach the end or find a piece
        X = self.x-1
        Y = self.y
        while(X >= 0):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1
        #check every tile along x-positive y-positive until you either reach the end or find a piece
        X = self.x+1
        Y = self.y+1
        while(Y < 8 and X < 8):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y+1
            X = X+1
        #check every tile along x-positive y-negative until you either reach the end or find a piece
        X = self.x+1
        Y = self.y-1
        while(Y >= 0 and X < 8):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            Y = Y-1
            X = X+1
        #check every tile along x-negative y-positive until you either reach the end or find a piece
        X = self.x-1
        Y = self.y+1
        while(X >= 0 and Y < 8):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1
            Y = Y+1
        #check every tile along x-negative y-negative until you either reach the end or find a piece
        X = self.x-1
        Y = self.y-1
        while(X >= 0 and Y >= 0):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
                break
            toReturn.append([X,Y])
            X = X-1
            Y = Y-1

class King(Piece):
    value = 10000000
    def getAvailableMoves(self, board):
        toReturn = []

        X = self.x+1
        Y = self.y+1
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x+1
        Y = self.y
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x+1
        Y = self.y-1
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x
        Y = self.y+1
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x
        Y = self.y-1
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x-1
        Y = self.y-1
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x-1
        Y = self.y+1
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        X = self.x-1
        Y = self.y
        if inBounds(X,Y):
            if board.board[X][Y].hasPiece():
                if board.board[X][Y].hasEnemyPiece(self.color):
                    toReturn.append([X,Y])
            else:
                toReturn.append([X,Y])
        return toReturn
