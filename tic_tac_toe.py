"""
Tic-Tac-Toe AI
CodSoft AI Internship - Task 2

An unbeatable Tic-Tac-Toe AI built using the Minimax algorithm
with Alpha-Beta pruning. The human plays 'X', the AI plays 'O'.

Alpha-Beta pruning is used purely as a speed optimization — it
skips branches of the game tree that cannot possibly change the
final decision, without changing the result. This demonstrates
understanding of both game theory (Minimax) and basic search
optimization (Alpha-Beta pruning), as required by the task.
"""

import math

HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = board[i:i + 3]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 6:
            print("---+---+---")
    print()


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def check_winner(board):
    """Returns 'X', 'O', 'Draw', or None (game still in progress)."""
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if EMPTY not in board:
        return "Draw"
    return None


def minimax(board, depth, alpha, beta, is_maximizing):
    """
    Minimax with Alpha-Beta pruning.

    The AI (maximizing player) tries to maximize the score,
    the human (minimizing player) is assumed to try to minimize it.
    Scores favor faster wins and slower losses (using `depth`),
    so the AI plays optimally even among multiple winning paths.
    """
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    elif winner == HUMAN:
        return depth - 10
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, alpha, beta, False)
            board[move] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # Alpha-Beta pruning: cut off remaining branches
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, alpha, beta, True)
            board[move] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def best_move(board):
    """Finds the AI's optimal move using Minimax with Alpha-Beta pruning."""
    best_score = -math.inf
    move = None
    for candidate in available_moves(board):
        board[candidate] = AI
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[candidate] = EMPTY
        if score > best_score:
            best_score = score
            move = candidate
    return move


def get_human_move(board):
    while True:
        raw = input(f"Your move ({HUMAN}) - choose a cell 1-9: ")
        if not raw.isdigit() or not (1 <= int(raw) <= 9):
            print("Please enter a number between 1 and 9.")
            continue
        pos = int(raw) - 1
        if board[pos] != EMPTY:
            print("That cell is already taken. Try again.")
            continue
        return pos


def print_position_guide():
    print("Cell positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")


def play():
    board = [EMPTY] * 9
    print("=== Tic-Tac-Toe: You (X) vs Unbeatable AI (O) ===")
    print_position_guide()

    while True:
        # Human move
        move = get_human_move(board)
        board[move] = HUMAN
        print_board(board)

        winner = check_winner(board)
        if winner:
            announce(winner)
            break

        # AI move
        print("AI is thinking...")
        ai_pos = best_move(board)
        board[ai_pos] = AI
        print(f"AI plays position {ai_pos + 1}")
        print_board(board)

        winner = check_winner(board)
        if winner:
            announce(winner)
            break


def announce(winner):
    if winner == "Draw":
        print("It's a draw! The AI cannot be beaten, only tied.")
    elif winner == HUMAN:
        print("You won?! (This shouldn't be possible against a perfect AI.)")
    else:
        print("AI wins!")


if __name__ == "__main__":
    play()
