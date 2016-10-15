from Grid import *
from Engine import *

class Game:

	def __init__(self, **kwargs):
		self.grid = Grid(kwargs.get("boardSize")[0], kwargs.get("boardSize")[1])
		self.engine = Engine()
		self.elements = []

	#sets elements' positions on the grid
	def updateGrid(self):
		print("updating grid...")
		for element in self.elements:
			self.grid[element.pos] = element.state

	#increments the game step. computes the next delta t=1step state
	def advance(self):
		print("advancing step...")
		for element in self.elements: element.proposeAction()
		self.engine.resolveActions(self.elements)
		self.updateGrid()

	def init(self):
		print("initialising basic game")
		self.elements.append(Element(Pos.element1Spawner, (0, int(self.grid.y/2))))
		self.elements.append(Element(Pos.element2Spawner, (self.grid.x-1, int(self.grid.y/2))))
		self.updateGrid()









