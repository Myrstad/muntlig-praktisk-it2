import unittest
from board import Board

class TestCalculatorMethods(unittest.TestCase):
  def test_size(self):
    self.assertEqual(len(Board(10, 10).grid), 100)
    self.assertEqual(len(Board(4, 100).grid), 400)

  def test_set(self):
    pass

  def test_emptying_grid(self):
    pass

  def test_get(self):
    pass

  def test_position_index_converting(self):
    pass