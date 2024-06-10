import random as rand

class Board(object):
  def __init__(self, rows, columns) -> None:
    #1 er levende, 0 er død, 33% s
    self.grid = [None for _ in range(columns) for _ in range(rows)]
    #kolonner og rader
    self.columns = columns
    self.rows = rows
  
  def init_grid_to_value(self, value) -> None:
    self.grid = [value for _ in self.grid]
  
  def empty_grid(self) -> None:
    self.grid = [None for _ in range(self.grid)]

  def position_to_index(self, x, y):
    return y*self.columns + x

  def index_to_position(self, index):
    return (index - index//self.columns*self.columns, index//self.columns)

  def get_value_from_index(self, index) -> bool:
    if index < 0:
      return 0
    if index >= len(self.grid):
      return 0
    return self.grid[index]

  def get_values_around(self, x:int, y:int) -> list:
    """Henter 'relative' posisjonene rundt posisjonen (x,y)
    følger rekkefølgen fra venstre til høyre, fra opp til ned.

    Args:
        x (int): posisjonens x-verdi
        y (int): posisjonens y-verdi

    Returns:
        list: verdiene rundt posisjonen
    """
    indexes = [] #indeksene til brettets .grid
    for _x in range(-1, 2):
      for _y in range(-1, 2):
        if _x == 0 and _y == 0:
          #skal ikke hente med seg selv
          continue
        #relative posisjoner
        rx = _x + x
        ry = _y + y
        #hvis posisjonen er utenfor rammene til brettet
        if rx == -1 or ry == -1 or rx >= self.columns or ry >= self.rows:
          continue
        indexes.append(self.position_to_index(rx, ry))
    
    return [self.get_value_from_index(idx) for idx in indexes]

