import copy

class BoardState:
    def __init__(self):
        self.blackKing = None
        self.whiteKing = None
        self.blackPieces = []
        self.whitePieces = []

    def __str__(self):
        final_string = ''
        # board[row][column
        board = [
            ['-'] * 8,
            ['-'] * 8,
            ['-'] * 8,
            ['-'] * 8,
            ['-'] * 8,
            ['-'] * 8,
            ['-'] * 8,
            ['-'] * 8]
        for piece in self.blackPieces:
            board[piece.y][piece.x] = piece.black_abb
        for piece in self.whitePieces:
            board[piece.y][piece.x] = piece.white_abb

        for row in board:
            final_string = final_string + "\n"
            for col in row:
                final_string = final_string + " " + col + " "

        return final_string

    #returns the color of the piece at the givin location, or 'none' if there is no piece at that location
    def pieceAt(self, x, y):
        for i in self.blackPieces:
            if i.x == x and i.y == y:
                return 'black'
        for i in self.whitePieces:
            if i.x == x and i.y == y:
                return 'white'
        return 'none'

    #returns the piece at the givin location, or None if there isn't one
    def getPieceAt(self, x, y):
        for i in self.blackPieces:
            if i.x == x and i.y == y:
                return i
        for i in self.whitePieces:
            if i.x == x and i.y == y:
                return i
        return None

    #returns the list of pieces of a givin color
    def getColorPieces(self, color):
        if color == 'white':
            return self.whitePieces
        else:
            return self.blackPieces

    def inCheck(self, color):
        if color == 'white':
            king_location = [self.whiteKing.x, self.whiteKing.y]
            for i in self.blackPieces:
                if king_location in i.getAvailableMoves(self):
                    return True
        else:
            king_location = [self.blackKing.x, self.blackKing.y]
            for i in self.whitePieces:
                if king_location in i.getAvailableMoves(self):
                    return True
        return False

    def inCheckMate(self, color):
        if color == 'white':
            for i in self.whitePieces:
                for j in i.getAvailableMoves(self):
                    if not self.stateAfterMove(i.x, i.y, j[0], j[1]).inCheck('white'):
                        return False
        else:
            for i in self.blackPieces:
                for j in i.getAvailableMoves(self):
                    if not self.stateAfterMove(i.x, i.y, j[0], j[1]).inCheck('black'):
                        return False
        return True


    #returns a copy of the BordState after the specified move has been made
    def stateAfterMove(self, xFrom, yFrom, xTo, yTo):
        newState = copy.deepcopy(self)
        newState.removePieceAt(xTo, yTo)
        newState.getPieceAt(xFrom, yFrom).setPosition(xTo, yTo)
        return newState
        
    #removes a piece from the board at the givin location and returns it, returns None if therewas no piece
    def removePieceAt(self, x, y):
        for i in range(len(self.blackPieces)):
            if self.blackPieces[i].x == x and self.blackPieces[i].y == y:
                return self.blackPieces.pop(i)
        for i in range(len(self.whitePieces)):
            if self.whitePieces[i].x == x and self.whitePieces[i].y == y:
                return self.whitePieces.pop(i)
        return None

    #adds a piece to the board
    def addPiece(self, piece):
        if piece.color == 'white':
            self.whitePieces.append(piece)
        else:
            self.blackPieces.append(piece)

    #returns an integer value that is the value of the board in reference to the givin color
    def evaluate(self, color):
        evaluation = 0
        white_evaluation = 0
        black_evaluation = 0

        # Material = Value of Pieces, Mobility = Available moves for each piece
        material_white = 0
        mobility_white = 0
        material_black = 0
        mobility_black = 0
        check_black = 0
        check_white = 0
        mate_black = 0
        mate_white = 0

        if self.inCheck('white'):
            check_white = 100000000
        if self.inCheck('black'):
            check_black = 100000000
        if self.inCheckMate('white'):
            check_white = 100000000
        if self.inCheckMate('black'):
            check_black = 100000000

        for piece in self.blackPieces:
            material_black = material_black + piece.value
            mobility_black = mobility_black + len(piece.getAvailableMoves(self)) * 10

        black_evaluation = material_black + mobility_black + check_white + mate_white

        for piece in self.whitePieces:
            material_white = material_white + piece.value
            mobility_white = mobility_white + len(piece.getAvailableMoves(self)) * 10

        white_evaluation = material_white + mobility_white + check_black + mate_black

        if color == 'black':
           evaluation = black_evaluation - white_evaluation
        else:
           evaluation = white_evaluation - black_evaluation
        return evaluation