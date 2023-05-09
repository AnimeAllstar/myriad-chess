import chess
from fastapi import FastAPI, Response, status, Request
from pydantic import ValidationError

from api_types import Game


# ChessBoardValidationMiddleware is a middleware that validates FEN strings,
# initializes chess boards, and attaches them to the request's state.
class ChessBoardValidationMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, request: Request, call_next: callable):
        # Check if the request is for an API route and uses POST method
        if request.url.path.startswith('/api/') and request.method == 'POST':
            try:
                # Parse the request body into a Game object and create a chess.Board
                body = await request.json()
                game = Game.parse_obj(body)
                board = chess.Board(game.fen)
            except (ValueError, ValidationError) as e:
                # If parsing or creating the board fails, return a 400 Bad Request response
                return Response(str(e), status_code=status.HTTP_400_BAD_REQUEST)

            # Check if the board's FEN is valid
            if not board.is_valid():
                return Response('Invalid FEN', status_code=status.HTTP_400_BAD_REQUEST)

            # Check if the game is already over
            if board.is_game_over():
                return Response('Game Over', status_code=status.HTTP_400_BAD_REQUEST)

            # Attach the chess.Board object to the request's state
            request.state.board = board

        # Proceed to the next middleware or route handler
        response = await call_next(request)

        return response


# get_board is a FastAPI dependency function that retrieves the chess.Board object
# attached to a request's state by the ChessBoardValidationMiddleware.
def get_board(request: Request) -> chess.Board:
    """
    Retrieve the chess.Board object from the request's state.

    Args:
        request (Request): FastAPI request object.

    Returns:
        chess.Board: The chess board associated with the request.
    """
    return request.state.board