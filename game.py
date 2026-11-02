"""Console Tic-Tac-Toe with a computer opponent (minimax algorithm)."""

import random

EMPTY = " "
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]
DIFFICULTIES = {"1": "easy", "2": "medium", "3": "hard"}


def new_board():
    return [EMPTY] * 9


def other(player):
    return "O" if player == "X" else "X"


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def winner(board):
    """Return 'X' or 'O' if someone has won, otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    return winner(board) is None and not available_moves(board)


def minimax(board, player, me):
    """Score the position for `me`, with `player` to move.

    A win scores more the sooner it happens, a loss less the later it happens,
    so the AI wins fast and resists losing as long as possible.
    """
    won = winner(board)
    empty = len(available_moves(board))
    if won == me:
        return empty + 1
    if won is not None:
        return -(empty + 1)
    if empty == 0:
        return 0

    scores = []
    for move in available_moves(board):
        board[move] = player
        scores.append(minimax(board, other(player), me))
        board[move] = EMPTY
    return max(scores) if player == me else min(scores)


def best_move(board, player):
    """Pick the strongest move; ties are broken randomly for variety."""
    best_score = None
    best = []
    for move in available_moves(board):
        board[move] = player
        score = minimax(board, other(player), player)
        board[move] = EMPTY
        if best_score is None or score > best_score:
            best_score, best = score, [move]
        elif score == best_score:
            best.append(move)
    return random.choice(best)


def ai_move(board, player, difficulty):
    moves = available_moves(board)
    if difficulty == "easy":
        return random.choice(moves)
    if difficulty == "medium" and random.random() < 0.5:
        return random.choice(moves)
    return best_move(board, player)


def render(board):
    """Show the board; free cells display their number (1-9)."""
    cells = [board[i] if board[i] != EMPTY else str(i + 1) for i in range(9)]
    rows = [f" {cells[r]} | {cells[r + 1]} | {cells[r + 2]} " for r in (0, 3, 6)]
    return "\n---+---+---\n".join(rows)


def ask(prompt, valid):
    while True:
        answer = input(prompt).strip().upper()
        if answer in valid:
            return answer
        print(f"Please enter one of: {', '.join(valid)}")


def ask_move(board):
    free = [str(i + 1) for i in available_moves(board)]
    return int(ask("Your move (1-9): ", free)) - 1


def play_round(human, difficulty):
    """Play one game. Return 'human', 'ai' or 'draw'."""
    board = new_board()
    turn = "X"
    while True:
        print("\n" + render(board) + "\n")
        if turn == human:
            move = ask_move(board)
        else:
            move = ai_move(board, turn, difficulty)
            print(f"Computer plays {move + 1}")
        board[move] = turn

        won = winner(board)
        if won or is_draw(board):
            print("\n" + render(board) + "\n")
            if won == human:
                print("You win!")
                return "human"
            if won:
                print("Computer wins!")
                return "ai"
            print("It's a draw.")
            return "draw"
        turn = other(turn)


def main():
    print("=== Tic-Tac-Toe vs Computer ===")
    print("X always moves first.")
    score = {"human": 0, "ai": 0, "draw": 0}
    while True:
        human = ask("Play as X or O? ", ["X", "O"])
        level = ask("Difficulty: 1 - easy, 2 - medium, 3 - hard: ", list(DIFFICULTIES))
        result = play_round(human, DIFFICULTIES[level])
        score[result] += 1
        print(f"Score: you {score['human']} | computer {score['ai']} | draws {score['draw']}")
        if ask("Play again? (Y/N) ", ["Y", "N"]) == "N":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
