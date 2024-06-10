class Board(object):
  """
  Board er en generell brettklasse som kan bruker til alle brettspill,
  eller spill der et brett kan brukes som en abstraksjon.

  Eksempler på dette er "livets spill", "bondesjakk", "fire på rad" og sjakk
  """
  def __init__(self, rows:int, columns:int) -> None:
    """__init__ konstruktør til Board (brett) klassen.

    Args:
        rows (int): antall rader
        columns (int): antall kolonner
    """
    #1 er levende, 0 er død, 33% s
    self.grid: list = [None for _ in range(columns) for _ in range(rows)]
    #kolonner og rader
    self.columns: int = columns
    self.rows: int = rows
  
  def init_grid_to_value(self, value:object) -> None:
    """Gjør om hele brettet til én verdi. 

    Args:
        value (object): any, hva som helst
    """
    self.grid = [value for _ in self.grid]
  
  def empty_grid(self) -> None:
    """Tømmer brettet."""
    self.grid = [None for _ in self.grid]

  def position_to_index(self, x:int, y:int) -> int:
    """position_to_index omgjøring fra posisjon til index.

    Args:
        x (int): x-posisjon
        y (int): y-posisjon

    Raises:
        ValueError: Ugyldig posisjon i brettet

    Returns:
        int: indeksen til posisjonen
    """
    if x < 0 or x >= self.columns or y < 0 or y >= self.rows:
      raise ValueError("Not a valid position")
    return y*self.columns + x

  def index_to_position(self, index) -> tuple[int, int]:
    """Gjør om indeks til tilsvarende posisjonen i brettet.

    Args:
        index (int): indeksen

    Raises:
        IndexError: ugyldig indeks, f.eks. negativ

    Returns:
        tuple[int, int]: posisjonen som svarer til indeksen
    """
    if index < 0 or index >= len(self.grid):
      raise IndexError
    return (index - index//self.columns*self.columns, index//self.columns)

  def get_value_from_index(self, index:int) -> object:
    """Henter verdi fra indeks til brettet.

    Args:
        index (int): indeksen

    Raises:
        IndexError: dersom indeksen er ugyldig

    Returns:
        object: any; hva som helst
    """
    if index < 0 or index >= len(self.grid):
      raise IndexError
    return self.grid[index]
  
  def set_index_to_value(self, index:int, value: object) -> None:
    """Setter indeksen i brettet til verdien

    Args:
        index (int): indeksen
        value (object): any, hva som helst

    Raises:
        IndexError: dersom indeksen er ugyldig
    """
    if index < 0 or index >= len(self.grid):
      raise IndexError
    self.grid[index] = value
