import copy

MAX_DEPTH = 2

def abMinMax(color, tree, minmax):
    if(len(tree.children) == 0):
        tree.eval = tree.state.evaluate(color)
        return tree
    else:
        evaluation = None
        for i in tree.children:
            if minmax == 'min':
                value = abMinMax(color, i, 'max')
                if evaluation is None or value.eval < evaluation.eval:
                    evaluation = value
            else:
                value = abMinMax(color, i, 'min')
                if evaluation is None or value.eval > evaluation.eval:
                    evaluation = value
        tree.eval = evaluation.eval
        if tree.parent == None:
            return evaluation
        else:
            return tree

class BoardState:
    def __init__(self):
        self.blackPieces = []
        self.whitePieces = []

    def __str__(self):
        str_return = '[[' + str(self.blackPieces[0])
        for i in range(1,len(self.blackPieces)):
            str_return = str_return + ',' + str(self.blackPieces[i])
        str_return = str_return + ']\n[' + str(self.whitePieces[0])
        for i in range(1,len(self.whitePieces)):
            str_return = str_return + ',' + str(self.whitePieces[i])
        return str_return + ']'

    def __repr__(self):
        str_return = '[[' + str(self.blackPieces[0])
        for i in range(1,len(self.blackPieces)):
            str_return = str_return + ',' + str(self.blackPieces[i])
        str_return = str_return + ']\n[' + str(self.whitePieces[0])
        for i in range(1,len(self.whitePieces)):
            str_return = str_return + ',' + str(self.whitePieces[i])
        return str_return + ']'

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

