import random as rand
import pygame as pg
from board import Board

class GameOfLife(Board):
  def __init__(self, rows:int, columns:int, CELL_SIZE:int, init_pygame:bool = True) -> None:
    """__init__ konstruktør til "spillets liv"

    Args:
        rows (int): antall rader
        columns (int): antall kolonner
        CELL_SIZE (int): størrelse på spill-rutene
        init_PyGame (bool, optional): Om spillet skal initialiseres. Settes til True om ikke spesifisert.
    """
    super().__init__(rows, columns)
    
    #1 er levende, 0 er død, 33% sjanse for levende
    #gjør grenseverdiene fra [0,1) til [0,0.667) avrunding gir altså 33% sjanse for 1, altså levende
    self.grid: list[bool] = [round(rand.random()/3*2) for _ in range(len(self.grid))]

    if init_pygame:
      #til tegning
      self.WIDTH: int = columns * CELL_SIZE
      self.HEIGHT: int = rows * CELL_SIZE
      self.CELL_SIZE: int = CELL_SIZE
      #til PyGame
      self.screen: pg.Surface = pg.display.set_mode((self.WIDTH, self.HEIGHT))
      pg.display.set_caption("Game Of Life | Myrstad")
      self._FPS: int = 60
      self.clock: pg.time.Clock = pg.time.Clock()
  
  def get_empty_grid(self) -> list:
    """Gjør hele brettet tomt, alle cellene er altså døde.

    Returns:
        list[]: helt tomt brett, liste med kun 0-er
    """
    return [0 for _ in self.grid]
  

  def get_alive_around(self, x:int, y:int) -> int:
    """Finner (gyldige) posisjoner rundt posisjonen (x,y) og teller antall levende

    Args:
        x (int): posisjonens x-verdi
        y (int): posisjonens y-verdi

    Returns:
        int: hvor mange celler rundt cellen (x,y) er i live
    """
    indexes = [] #indeksene til brettets grid
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
    
    #sjekker hvor mange som er i live
    return [self.get_value_from_index(idx) for idx in indexes].count(1)
  
  def rules(self, alive_around:int, is_currently_alive:bool) -> bool:
    """Sjekker om en celle utifra informasjon skal dø eller leve.

    Args:
        alive_around (int): hvor mange celler rundt cellen som nå lever
        is_currently_alive (bool): om celler nå er i live

    Returns:
        bool: hvilken tilstand cellen skal ha, i neste generasjons
    """
    #uansett død uansett om cellen er / ikke er i live
    if alive_around < 2 or alive_around > 3:
      return 0
    
    #hvis cellen IKKE skal gjenopplives
    if alive_around == 2 and not is_currently_alive:
      return 0
    
    #hvis cellen skal gjenopplives eller holdes i live
    return 1

  def next_generation(self) -> list[bool]:
    """Lager neste iterasjon av spillet.

    Returns:
        list[bool]: brettets neste generasjon
    """
    temporary_grid: list[bool] = self.get_empty_grid()
    for x in range(self.columns):
      for y in range(self.rows):
        index = self.position_to_index(x, y)
        temporary_grid[index] = self.rules(
          self.get_alive_around(x, y), self.get_value_from_index(index)
        )
    return temporary_grid

  def draw_grid(self) -> None:
    """Tegner brettet til spillet."""
    for index in range(len(self.grid)):
      x, y = self.index_to_position(index)
      x*= self.CELL_SIZE
      y*= self.CELL_SIZE
      if self.get_value_from_index(index):
        pg.draw.rect(self.screen, "black", (x,y,x+self.CELL_SIZE,y+self.CELL_SIZE))
      else:
        pg.draw.rect(self.screen, "white", (x,y,x+self.CELL_SIZE,y+self.CELL_SIZE))
        pg.draw.rect(self.screen, "grey", (x,y,x+self.CELL_SIZE,y+self.CELL_SIZE), 1)
  
  def loop(self) -> None:
    """Hoved spill løkken."""
    running = True
    while running:
      self.screen.fill("white") #maler skjermen hvitt (bakgrunnsfarge)
      self.clock.tick(self._FPS) #kjører 60 FPS

      for event in pg.event.get():
        if event.type == pg.QUIT: #hvis vindu krysses ut
          running = False
        if event.type == pg.KEYDOWN: #hvis tastaturet blir trykket på
          if event.key == pg.K_ESCAPE:
            running = False
          if event.key == pg.K_BACKSPACE:
            #ved backspace tømmes brettet
            self.grid = self.get_empty_grid()
          if event.key == pg.K_RETURN:
            #ved return spilles neste generasjon
            self.grid = self.next_generation()
        if event.type == pg.MOUSEBUTTONDOWN:
          #ruten som trykkes endres fra motsatt av hva den er, eks. hvis død så blir den levende
          x,y = event.pos
          x = x // self.CELL_SIZE
          y = y // self.CELL_SIZE
          index = self.position_to_index(x,y)
          self.grid[index] = not self.grid[index]

      self.draw_grid() #tegner brettet

      pg.display.flip() #oppdater skjermen

def main():
  game = GameOfLife(20, 30, 30)
  game.loop()

if __name__ == '__main__':
  main()