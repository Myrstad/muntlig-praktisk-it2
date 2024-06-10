import unittest
from board import Board

class TestCalculatorMethods(unittest.TestCase):
  def test_size(self):
    self.assertEqual(len(Board(10, 10).grid), 100)
    self.assertEqual(len(Board(4, 100).grid), 400)

  def test_set_and_get(self):
    board = Board(10, 10)
    board.set_value_from_index(0, "a")
    board.set_value_from_index(10, "b")

    self.assertEqual(board.get_value_from_index(0), "a")
    self.assertEqual(board.get_value_from_index(10), "b")

  def test_init_and_emptying_grid(self):
    board = Board(3, 3)
    self.assertEqual(board.grid, [None,None,None,None,None,None,None,None,None])
    board.init_grid_to_value("t")
    self.assertEqual(board.grid, ["t","t","t","t","t","t","t","t","t"])
    board.empty_grid()
    self.assertEqual(board.grid, [None,None,None,None,None,None,None,None,None])

  def test_index_to_position(self):
    board = Board(3, 3)
    self.assertEqual(board.index_to_position(0), (0,0))
    self.assertEqual(board.index_to_position(1), (1,0))
    self.assertEqual(board.index_to_position(2), (2,0))
    self.assertEqual(board.index_to_position(3), (0,1))
    self.assertEqual(board.index_to_position(4), (1,1))
    self.assertEqual(board.index_to_position(5), (2,1))
    self.assertEqual(board.index_to_position(6), (0,2))
    self.assertEqual(board.index_to_position(7), (1,2))
    self.assertEqual(board.index_to_position(8), (2,2))

  def test_position_to_index(self):
    board = Board(3, 3)
    self.assertEqual(board.position_to_index(0,0), 0)
    self.assertEqual(board.position_to_index(1,0), 1)
    self.assertEqual(board.position_to_index(2,0), 2)
    self.assertEqual(board.position_to_index(0,1), 3)
    self.assertEqual(board.position_to_index(1,1), 4)
    self.assertEqual(board.position_to_index(2,1), 5)
    self.assertEqual(board.position_to_index(0,2), 6)
    self.assertEqual(board.position_to_index(1,2), 7)
    self.assertEqual(board.position_to_index(2,2), 8)
  
  def test_error_handling(self):
    board = Board(3, 3)
    with self.assertRaises(IndexError):
      board.index_to_position(-1)
    with self.assertRaises(IndexError):
      board.index_to_position(9)
    with self.assertRaises(ValueError):
      board.position_to_index(-1, 0)
    with self.assertRaises(ValueError):
      board.position_to_index(0, -2)
    with self.assertRaises(ValueError):
      board.position_to_index(3, 0)
    with self.assertRaises(ValueError):
      board.position_to_index(0, 3)