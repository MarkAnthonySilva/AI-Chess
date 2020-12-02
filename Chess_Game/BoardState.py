


class Tile:
    def __init__(self, X, Y, Color):
        self.x = X
        self.y = Y
        self.color = Color
        self.piece = None

    def setCurrentPiece(self, Piece):
        self.piece = Piece

    def hasPiece(self):
        return self.piece is not None

    def hasEnemyPiece(self, color):
        if(self.piece is not None):
            if(self.piece.color == color):
                return False
            else:
                return True
        else:
            return False



class BoardState:
    def __init__(self):
        self.board = [[],[],[],[],[],[],[],[]]
        currentColor = 'white'
        for i in range(8):
            for j in range(8):
                self.board[i].append(Tile(i,j, currentColor))
                if(currentColor == 'white'):
                    currentColor = 'black'
                else:
                    currentColor = 'white'
            if(currentColor == 'white'):
                currentColor = 'black'
            else:
                currentColor = 'white'

    def evaluate(self, color):
        #return the value of the boardstate in relation to the color passed along
        value = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j].hasPiece:
                    if self.board[i][j].piece.color == color:
                        value = value + self.board[i][j].piece.value
                    else:
                        value = value - self.board[i][j].piece.value
        return value

