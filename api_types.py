"""This module contains Pydantic models that represent types used by the API."""
from pydantic import BaseModel


class Game(BaseModel):
    """
    A Pydantic model representing the state of a chess game.

    Attributes:
        fen (str): A string containing the FEN (Forsyth-Edwards Notation)
                   representation of the game's current state.
    """

    fen: str


class MoveResponse(BaseModel):
    """
    A Pydantic model representing the response structure for move-related API endpoints.

    Attributes:
        fen (str): A string containing the FEN (Forsyth-Edwards Notation)
                   representation of the game's current state.
        move (str): A string containing the UCI (Universal Chess Interface) notation
                    of the move that was made.
    """

    fen: str
    move: str
