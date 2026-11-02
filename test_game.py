import unittest

from game import EMPTY, ai_move, best_move, is_draw, new_board, other, winner


def board_from(text):
    """Build a board from a 9-char string, '.' meaning empty."""
    return [EMPTY if c == "." else c for c in text]


class WinnerTests(unittest.TestCase):
    def test_empty_board_has_no_winner(self):
        self.assertIsNone(winner(new_board()))

    def test_row_column_and_diagonal(self):
        self.assertEqual(winner(board_from("XXX......")), "X")
        self.assertEqual(winner(board_from("O..O..O..")), "O")
        self.assertEqual(winner(board_from("..X.X.X..")), "X")

    def test_draw(self):
        board = board_from("XOXXOOOXX")
        self.assertIsNone(winner(board))
        self.assertTrue(is_draw(board))


class AITests(unittest.TestCase):
    def test_takes_winning_move(self):
        self.assertEqual(best_move(board_from("OO.XX...."), "O"), 2)

    def test_blocks_opponent(self):
        self.assertEqual(best_move(board_from("XX..O...."), "O"), 2)

    def test_easy_ai_plays_legal_move(self):
        board = board_from("XOXOX....")
        for _ in range(20):
            self.assertIn(ai_move(board, "O", "easy"), [5, 6, 7, 8])

    def test_hard_ai_never_loses(self):
        """Try every possible human strategy against the hard AI."""

        def explore(board, turn, ai):
            won = winner(board)
            if won:
                self.assertEqual(won, ai, f"AI lost on board {board}")
                return
            if is_draw(board):
                return
            if turn == ai:
                board[best_move(board, ai)] = ai
                explore(board, other(turn), ai)
            else:
                for move in [i for i, c in enumerate(board) if c == EMPTY]:
                    child = board.copy()
                    child[move] = turn
                    explore(child, other(turn), ai)

        explore(new_board(), "X", "O")  # AI moves second
        explore(new_board(), "X", "X")  # AI moves first


if __name__ == "__main__":
    unittest.main()
