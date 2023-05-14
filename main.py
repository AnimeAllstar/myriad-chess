"""Entry point for the FastAPI application."""
import random

import chess
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from api_types import MoveResponse
from middlewares import chess_board_validation_middleware, get_board
from search_tree_algorithms import minimax

app = FastAPI()

# List of origins that are allowed to make requests to this API
origins = [
    "http://localhost",
    "http://localhost:3000",
]

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add board validation middleware to validate the chess board state
app.middleware("http")(chess_board_validation_middleware)


@app.get("/")
async def root():
    """
    Root endpoint that returns a simple greeting message.
    """
    return "Hello World"


def log_move(board: chess.Board, move: chess.Move):
    """
    Log the current board state and the chosen move.

    :param board: A chess board object with the current game state.
    :param move: The chosen move as a chess.Move object.
    """
    print(f"fen: {board.fen()}, move: {move.uci()}")


@app.post("/api/random")
async def random_ai(board: chess.Board = Depends(get_board)) -> MoveResponse:
    """
    API route for making a random move on the chessboard.
    The move is chosen randomly from the list of legal moves.

    :param board: A chess board object with the current game state.
    :return: A MoveResponse object with the updated FEN and the chosen move.
    """
    move = random.choice(list(board.legal_moves))
    board.push(move)

    log_move(board, move)
    return MoveResponse(fen=board.fen(), move=move.uci())


@app.post("/api/minimax/{depth}")
async def minimax_ai(depth: int, board: chess.Board = Depends(get_board)) -> MoveResponse:
    """
    API route for making a move on the chessboard using the minimax algorithm
    with a specified search depth.

    :param depth: The search depth for the minimax algorithm.
    :param board: A chess board object with the current game state.
    :return: A MoveResponse object with the updated FEN and the chosen move.
    """
    move, _ = minimax(board, depth, float("-inf"), float("inf"), True)
    best_move = chess.Move.from_uci(move)
    board.push(best_move)

    log_move(board, best_move)
    return MoveResponse(fen=board.fen(), move=best_move.uci())
