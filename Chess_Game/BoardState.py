import copy

MAX_DEPTH = 2

class BoardState:
    def __init__(self):
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
    def pieceAt(self, x, y):
        for i in self.blackPieces:
            if i.x == x and i.y == y:
                return 'black'
        for i in self.whitePieces:
            if i.x == x and i.y == y:
                return 'white'
        return 'none'

    def getPieceAt(self, x, y):
        for i in self.blackPieces:
            if i.x == x and i.y == y:
                return i
        for i in self.whitePieces:
            if i.x == x and i.y == y:
                return i
        return None

    def addPiece(self, piece):
        if piece.color == 'white':
            self.whitePieces.append(piece)
        else:
            self.blackPieces.append(piece)


    def evaluate(self, color):
        evaluation = 0
        white_evaluation = 0
        black_evaluation = 0

        # Material = Value of Pieces plus position, Mobility = Available moves for each piece
        material_white = 0
        mobility_white = 0
        material_black = 0
        mobility_black = 0

        for piece in self.blackPieces:
            piece_table = piece.getPointTable()
            x = piece.x
            y = piece.y
            row = piece_table[x]
            value = row[y]

            material_black = material_black + piece.value + -value
            mobility_black = mobility_black + len(piece.getAvailableMoves(self)) * 10
        black_evaluation = material_black + mobility_black

        for piece in self.whitePieces:
            piece_table = piece.getPointTable()
            x = piece.x
            y = piece.y
            row = piece_table[x]
            value = row[y]

            material_white = material_white + piece.value + value
            mobility_white = mobility_white + len(piece.getAvailableMoves(self)) * 10
        white_evaluation = material_white + mobility_white

        if color == 'black':
           evaluation = black_evaluation - white_evaluation
        else:
           evaluation = white_evaluation - black_evaluation
        return evaluation

    def createTree(self, color):
        root = StateTree(self)
        treeRecursion(color, 0, root)
        return root
        
                    

class StateTree:
    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent
        self.children = []
        self.eval = 0

def treeRecursion(color, depth, state):
    board = state.state
    if color == 'white':
        #iterate through all the pieces
        for i in board.whitePieces:
            #for each piece, get all the available moves
            possibleMoves = i.getAvailableMoves(board)
            #for every possible move, create a copy of the state, make the move, then append it to the parent state
            for j in possibleMoves:
                cp = copy.deepcopy(board)
                piece = cp.getPieceAt(i.x, i.y)
                #if there is already a piece there, remove it
                if cp.pieceAt(j[0],j[1]) == 'black':
                    for k in range(len(cp.blackPieces)):
                        if cp.blackPieces[k].x == j[0] and cp.blackPieces[k].y == j[1]:
                            cp.blackPieces.pop(k)
                            break
                piece.x = j[0]
                piece.y = j[1]
                piece.moved = True
                state.children.append(StateTree(cp,state))
    else:
        #iterate through all the pieces
        for i in board.blackPieces:
            #for each piece, get all the available moves
            possibleMoves = i.getAvailableMoves(board)
            #for every possible move, create a copy of the state, make the move, then append it to the parent state
            for j in possibleMoves:
                cp = copy.deepcopy(board)
                piece = cp.getPieceAt(i.x, i.y)
                #if there is already a piece there, remove it
                if cp.pieceAt(j[0],j[1]) == 'white':
                    #cp.whitePieces.remove(board.pieceAt(j[0],j[1]))
                    for k in range(len(cp.blackPieces)):
                        if cp.whitePieces[k].x == j[0] and cp.whitePieces[k].y == j[1]:
                            cp.whitePieces.pop(k)
                            break
                piece.x = j[0]
                piece.y = j[1]
                piece.moved = True
                state.children.append(StateTree(cp,state))
    if depth < MAX_DEPTH:
        for i in state.children:
            if color == 'black':
                treeRecursion('white', depth + 1, i)
            else:
                treeRecursion('black', depth + 1, i)

