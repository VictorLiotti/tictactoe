# test_tictactoe.py
# Unit tests for the TicTacToe game logic using the unittest module.

import unittest
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board_is_empty(self):
        self.assertEqual(self.game.board, [''] * 9)

    def test_valid_move(self):
        self.assertTrue(self.game.is_valid_move(1))
        self.assertTrue(self.game.make_move(1))
        self.assertFalse(self.game.is_valid_move(1))

    def test_invalid_move_out_of_range(self):
        self.assertFalse(self.game.is_valid_move(0))
        self.assertFalse(self.game.is_valid_move(10))

    def test_make_move_and_current_player(self):
        symbol = self.game.current_player
        self.assertTrue(self.game.make_move(1))
        self.assertEqual(self.game.board[0], symbol)

    def test_winning_row(self):
        self.game.board = ['X', 'X', 'X', '', '', '', '', '', '']
        self.assertTrue(self.game.has_winner('X'))
        self.assertEqual(self.game.winner, 'X')
        self.assertTrue(self.game.game_over)

    def test_winning_column(self):
        self.game.board = ['O', '', '', 'O', '', '', 'O', '', '']
        self.assertTrue(self.game.has_winner('O'))

    def test_winning_diagonal(self):
        self.game.board = ['X', '', '', '', 'X', '', '', '', 'X']
        self.assertTrue(self.game.has_winner('X'))

    def test_no_winner_on_empty_board(self):
        self.assertFalse(self.game.has_winner())

    def test_is_board_full_true(self):
        self.game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        self.assertTrue(self.game.is_board_full())

    def test_is_board_full_false(self):
        self.game.board = ['X', 'O', 'X', 'O', '', 'O', 'X', 'O', 'X']
        self.assertFalse(self.game.is_board_full())

    def test_minimax_block_win(self):
        self.game.user_symbol = 'X'
        self.game.opponent_symbol = 'O'
        self.game.board = ['X', 'X', '', '', 'O', '', '', '', '']
        _, move = self.game.minimax(0, True)
        self.assertEqual(move, 3)  # block at position 3

    def test_minimax_take_win(self):
        self.game.user_symbol = 'X'
        self.game.opponent_symbol = 'O'
        self.game.board = ['O', 'O', '', '', 'X', '', '', '', '']
        _, move = self.game.minimax(0, True)
        self.assertEqual(move, 3)  # win at position 3

    def test_computer_move_easy(self):
        self.game.difficulty = 'easy'
        self.game.user_symbol = 'X'
        self.game.user_index = 2
        self.game.computer_move()
        self.assertIn('O', self.game.board)

    def test_computer_move_normal(self):
        self.game.difficulty = 'normal'
        self.game.user_symbol = 'X'
        self.game.user_index = 2
        # Setup board so computer should block or try to win (block in this case)
        self.game.board = ['X', 'X', '', '', 'O', '', '', '', '']
        self.game.computer_move()
        self.assertEqual(self.game.board[2], 'O')

    def test_computer_move_hard(self):
        self.game.difficulty = 'hard'
        self.game.user_symbol = 'X'
        self.game.user_index = 2
        self.game.computer_move()
        self.assertIn('O', self.game.board)
    
    def test_game_draw(self):
        self.game.board = ['X','O','X','X','O','O','O','X','X']
        self.assertTrue(self.game.is_board_full())
        self.assertFalse(self.game.has_winner())

    def test_turn_and_current_player_switch(self):
        initial_player = self.game.current_player
        self.assertTrue(self.game.make_move(1))
        self.game.turn += 1  # if your code does not increment turn in make_move
        self.assertNotEqual(self.game.current_player, initial_player)

    def test_make_move_with_explicit_symbol(self):
        self.assertTrue(self.game.make_move(2, 'O'))
        self.assertEqual(self.game.board[1], 'O')

if __name__ == '__main__':
    unittest.main()
