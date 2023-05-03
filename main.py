import random

import chess
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Game(BaseModel):
    fen: str


app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def root():
    return 'Hello World'


@app.post('/api/random')
async def random_ai(game: Game, response: Response):
    try:
        board = chess.Board(game.fen)
    except ValueError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return 'Invalid FEN'

    if not board.is_valid():
        response.status_code = status.HTTP_400_BAD_REQUEST
        return 'Invalid FEN'

    if board.is_game_over():
        return {'fen': board.fen(), 'outcome': board.outcome()}

    move = random.choice(list(board.legal_moves))
    board.push(move)

    return {'fen': board.fen(), 'move': move.uci()}
