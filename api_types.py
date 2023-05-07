from pydantic import BaseModel


# The Game class is a Pydantic model that represents the state of a chess game.
# It is used for data validation (type checking) and serialization when handling API requests.
class Game(BaseModel):
    """
    A Pydantic model representing the state of a chess game.

    Attributes:
        fen (str): A string containing the FEN (Forsyth-Edwards Notation)
                   representation of the game's current state.
    """
    fen: str


# The MoveResponse class is a Pydantic model that represents the response structure
# for move-related API endpoints. It is used for data validation (type checking)
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
