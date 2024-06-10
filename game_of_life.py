import random as rand
from board.main import Board

class GameOfLife(Board):
  def __init__(self, rows, columns, CELL_SIZE) -> None:
    super().__init__(rows, columns)
    self.init_grid_to_value(round(rand.random()/3*2))

    self.WIDTH = columns * CELL_SIZE
    self.HEIGHT = rows * CELL_SIZE

def main():
  game = GameOfLife(30, 20, 30)
  print(game.grid)

if __name__ == '__main__':
  main()