import unittest
from game_of_life import GameOfLife

class TestCalculatorMethods(unittest.TestCase):
  def test_rules(self):
    game = GameOfLife(5, 5, 0)
    self.assertEqual(game.rules(0, True), 0)
    self.assertEqual(game.rules(1, True), 0)
    self.assertEqual(game.rules(2, True), 1)
    self.assertEqual(game.rules(3, True), 1)
    self.assertEqual(game.rules(4, True), 0)
    self.assertEqual(game.rules(5, True), 0)
    self.assertEqual(game.rules(6, True), 0)
    self.assertEqual(game.rules(7, True), 0)
    self.assertEqual(game.rules(8, True), 0)
    self.assertEqual(game.rules(0, False), 0)
    self.assertEqual(game.rules(1, False), 0)
    self.assertEqual(game.rules(2, False), 0)
    self.assertEqual(game.rules(3, False), 1)
    self.assertEqual(game.rules(4, False), 0)
    self.assertEqual(game.rules(5, False), 0)
    self.assertEqual(game.rules(6, False), 0)
    self.assertEqual(game.rules(7, False), 0)
    self.assertEqual(game.rules(8, False), 0)
  
  def test_game(self):
    #3x3 alternating
    game = GameOfLife(3, 3, None, False)
    game.grid = [
      0,1,0,
      0,1,0,
      0,1,0
    ]
    next_generation = [
      0,0,0,
      1,1,1,
      0,0,0
    ]
    self.assertEqual(game.next_generation(), next_generation)

    #4x4 stable
    game.columns = 4; game.rows = 4
    stable = [
      0,0,0,0,
      0,1,1,0,
      0,1,1,0,
      0,0,0,0
    ]
    game.grid = stable
    self.assertEqual(game.next_generation(), stable)