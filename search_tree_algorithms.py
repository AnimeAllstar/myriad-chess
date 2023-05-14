"""This Module contains the search tree algorithms implemented for the chess API."""
from typing import Tuple

import chess


def minimax(board: chess.Board, depth: int, alpha: float, beta: float, is_maximizing_player: bool) -> Tuple[str, int]:
    """
    Finds the best move for the current player using the minimax algorithm with alpha-beta pruning.

    Args:
        board (chess.Board): The current game state represented as a chess.Board object.
        depth (int): The search depth for the minimax algorithm.
        alpha (float): The best (maximum) value found so far for the maximizing player.
        beta (float): The best (minimum) value found so far for the minimizing player.
        is_maximizing_player (bool): True if the current player is the maximizing player, False otherwise.

    Returns:
        Tuple[str, int]: A tuple containing the best move in UCI notation (str) and the evaluation of that move (int).
    """
    # Base case: if the search depth is 0 or the game is over, return the current move and the number of legal moves
    if depth == 0 or board.is_game_over():
        return board.peek().uci(), board.legal_moves.count()

    # Maximizing player's turn
    if is_maximizing_player:
        max_eval = float("-inf")  # Initialize the maximum evaluation to negative infinity
        best_move = None  # Initialize the best move as None

        # Iterate through all legal moves
        for move in board.legal_moves:
            board.push(move)  # Make the move on the board
            current_eval = minimax(board, depth - 1, alpha, beta, False)[1]  # Get the evaluation of the move
            board.pop()  # Undo the move

            # Update the maximum evaluation and best move if the current evaluation is higher
            if current_eval > max_eval:
                max_eval = current_eval
                best_move = move

            alpha = max(alpha, current_eval)  # Update the alpha value
            if beta <= alpha:  # If beta is less than or equal to alpha, prune the remaining branches
                break

        return best_move.uci(), max_eval  # Return the best move and the maximum evaluation

    # Minimizing player's turn
    min_eval = float("inf")  # Initialize the minimum evaluation to positive infinity
    best_move = None  # Initialize the best move as None

    # Iterate through all legal moves
    for move in board.legal_moves:
        board.push(move)  # Make the move on the board
        current_eval = minimax(board, depth - 1, alpha, beta, True)[1]  # Get the evaluation of the move
        board.pop()  # Undo the move

        # Update the minimum evaluation and best move if the current evaluation is lower
        if current_eval < min_eval:
            min_eval = current_eval
            best_move = move

        beta = min(beta, current_eval)  # Update the beta value
        if beta <= alpha:  # If beta is less than or equal to alpha, prune the remaining branches
            break

    return best_move.uci(), min_eval  # Return the best move and the minimum evaluation
