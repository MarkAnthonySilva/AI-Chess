import chess
import chess_util
import math
import sys


def evaluate_board():
    # Assumption that AI is white
    if board.is_checkmate():
        if board.turn:  # White is checkmated
            return -9999
        else:           # Black is checkmated
            return 9999

    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    # Find the number of pieces
    wpawns      = len(board.pieces(chess.PAWN, chess.WHITE))
    wknights    = len(board.pieces(chess.KNIGHT, chess.WHITE))
    wbishop     = len(board.pieces(chess.BISHOP, chess.WHITE))
    wrook       = len(board.pieces(chess.ROOK, chess.WHITE))
    wqueen      = len(board.pieces(chess.QUEEN, chess.WHITE))
    bpawns      = len(board.pieces(chess.PAWN, chess.BLACK))
    bknights    = len(board.pieces(chess.KNIGHT, chess.BLACK))
    bbishop     = len(board.pieces(chess.BISHOP, chess.BLACK))
    brook       = len(board.pieces(chess.ROOK, chess.BLACK))
    bqueen      = len(board.pieces(chess.QUEEN, chess.BLACK))

    # Calculate point value considering the number of pieces each side has
    material = 100*(wpawns - bpawns) + 320*(wknights - bknights) + 330*(wbishop - bbishop) + 500*(wrook - brook) + \
               90*(wqueen - bqueen)

    eval = material
    if board.turn:
        return eval
    else:
        return -eval


def depthLimited_alpha_beta(alpha, beta, depthleft):
    bestscore = -sys.maxsize
    

def selectmove(depth):
    bestMove = chess.Move.null()
    bestValue = -sys.maxsize + 1
    alpha = -sys.maxsize
    beta = sys.maxsize


# Capital - White Player, Lower Case - Black Player
board = chess.Board()
print(board)
print(sys.maxsize)
print(-sys.maxsize)