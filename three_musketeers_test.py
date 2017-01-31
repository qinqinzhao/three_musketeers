import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual(string_to_location('B2'), (1, 1))
        self.assertEqual(string_to_location('E4'), (4, 3))

    def test_location_to_string(self):
        self.assertEqual(location_to_string((0, 2)), 'A3')
        self.assertEqual(location_to_string((3, 0)), 'D1')

    def test_at(self):
        self.assertEqual(at((0, 3)), 'M')
        self.assertEqual(at((3, 1)), 'R')
        self.assertEqual(at((4, 2)), '-')

    def test_all_locations(self):
        result = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                  (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                  (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                  (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                  (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        self.assertEqual(all_locations(), result)

    def test_adjacent_location(self):
        self.assertEqual(adjacent_location((2, 3), "up"), (1, 3))
        self.assertEqual(adjacent_location((2, 3), "down"), (3, 3))
        self.assertEqual(adjacent_location((2, 3), "left"), (2, 2))
        self.assertEqual(adjacent_location((2, 3), "right"), (2, 4))
        
    def test_is_legal_move_by_musketeer(self):
        self.assertTrue(is_legal_move_by_musketeer((2, 2), "left"))
        self.assertTrue(is_legal_move_by_musketeer((1, 3), "down"))
        self.assertFalse(is_legal_move_by_musketeer((0, 3), "right"))
        
    def test_is_legal_move_by_enemy(self):
        self.assertTrue(is_legal_move_by_enemy((2, 1), "left"))
        self.assertTrue(is_legal_move_by_enemy((2, 3), "down"))
        self.assertFalse(is_legal_move_by_enemy((1, 2), "right"))

    def test_is_legal_move(self):
        self.assertTrue(is_legal_move((2, 2), "left"))
        self.assertTrue(is_legal_move((2, 1), "left"))
        self.assertFalse(is_legal_move((1, 2), "right"))
        
    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertTrue(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))

    def test_possible_moves_from(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])
        self.assertEqual(possible_moves_from((1, 3)), ["down", "left"])
        self.assertEqual(possible_moves_from((2, 1)), ["up", "left"])
        self.assertEqual(possible_moves_from((4, 3)), ["up", "left", "right"])                

    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(can_move_piece_at((0, 3)))
        self.assertFalse(can_move_piece_at((1, 3)))
        self.assertTrue(can_move_piece_at((2, 2))) 

    def test_is_legal_location(self):
        self.assertTrue(is_legal_location((1, 2)))
        self.assertTrue(is_legal_location((3, 4)))
        self.assertFalse(is_legal_location((5, 5)))

    def test_is_within_board(self):
        self.assertTrue(is_within_board((0, 3), "right"))
        self.assertTrue(is_within_board((2, 2), "up"))
        self.assertFalse(is_within_board((1, 4), "right"))

    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        all_possible_moves_for_M = [((0, 3), "left"),
                                    ((0, 3), "right"),
                                    ((1, 4), "up")]
        self.assertEqual(all_possible_moves_for("M"), all_possible_moves_for_M)
        all_possible_moves_for_R = [((0, 2), "down"),
                                    ((0, 2), "left")]
        self.assertEqual(all_possible_moves_for("R"), all_possible_moves_for_R)
        
    def test_make_move(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])
        new_board_1 = ([ [_, _, _, M, _],
                         [_, R, R, M, _],
                         [_, _, M, R, _],
                         [_, R, _, _, _],
                         [_, _, _, R, _] ])
        self.assertEqual(make_move((2, 1), "up"), new_board_1)
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        new_board_2 = ([ [_, _, M, _, R],
                       [_, _, _, M, M],
                       [_, _, _, _, _],
                       [_, _, _, _, _],
                       [_, _, _, _, _] ] )
        self.assertEqual(make_move((0, 3), "left"), new_board_2)
        
    def test_choose_computer_move(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        all_possible_moves_for_M = [((0, 3), "left"),
                                    ((0, 3), "right"),
                                    ((1, 4), "up")]
        all_possible_moves_for_R = [((0, 2), "down"),
                                    ((0, 2), "left")]
        self.assertEqual(choose_computer_move("M"), ((0, 3), "left"))
        self.assertEqual(choose_computer_move("R"), ((0, 2), "down"))

    def test_is_enemy_win(self):
        self.assertFalse(is_enemy_win())
        set_board([ [_, _, M, M, _],
                    [_, _, _, _, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertFalse(is_enemy_win())
        set_board([ [_, _, M, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())

unittest.main()
