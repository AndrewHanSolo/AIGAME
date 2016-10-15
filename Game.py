from Grid import *

class Game:

	def __init__(self, **kwargs):
		self.grid = Grid(kwargs.get("boardSize")[0], kwargs.get("boardSize")[1])

