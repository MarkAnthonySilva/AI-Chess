


#class Tile:
#    def __init__(self, X, Y, Color):
#        self.x = X
#        self.y = Y
#        self.color = Color
#        self.piece = None

#    def setCurrentPiece(self, Piece):
#        self.piece = Piece

#    def hasPiece(self):
#        return self.piece is not None

#    def hasEnemyPiece(self, color):
#        if(self.piece is not None):
#            if(self.piece.color == color):
#                return False
#            else:
#                return True
#        else:
#            return False

class BoardState:
    def __init__(self):
        self.blackPieces = []
        self.whitePieces = []

    def pieceAt(self, x, y):
        for i in blackPieces:
            if i.x == x and i.y == y:
                return 'black'
        for i in whitePieces:
            if i.x == x and i.y == y:
                return 'white'
        return 'none'

    def addPiece(self, piece):
        if piece.color == 'white':
            self.whitePieces.append(piece)
        else:
            self.blackPieces.append(piece)

    def evaluate(self, color):
        evaluation = 0;
        if color == 'black':
            for i in self.blackPieces:
                evaluation == evaluation + i.value
            for i in self.whitePieces:
                evaluation == evaluation - i.value
        else:
            for i in self.blackPieces:
                evaluation == evaluation - i.value
            for i in self.whitePieces:
                evaluation == evaluation + i.value

class StateTree:
    def __init__(self, state, parent = None, children = None):
        self.state = state
        self.parent = parent
        if children is not None:
            self.children = children
        else:
            self.children = []



#class BoardState:
#    def __init__(self):
#        self.board = [[],[],[],[],[],[],[],[]]
#        currentColor = 'white'
#        for i in range(8):
#            for j in range(8):
#                self.board[i].append(Tile(i,j, currentColor))
#                if(currentColor == 'white'):
#                    currentColor = 'black'
#                else:
#                    currentColor = 'white'
#            if(currentColor == 'white'):
#                currentColor = 'black'
#            else:
#                currentColor = 'white'

#    def evaluate(self, color):
#        #return the value of the boardstate in relation to the color passed along
#        value = 0
#        for i in range(8):
#            for j in range(8):
#                if self.board[i][j].hasPiece:
#                    if self.board[i][j].piece.color == color:
#                        value = value + self.board[i][j].piece.value
#                    else:
#                        value = value - self.board[i][j].piece.value
#        return value

