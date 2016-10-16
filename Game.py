from Grid import *
import Engine
import random

class Game:

	def __init__(self, **kwargs):
		self.grid = Grid(kwargs.get("boardSize")[0], kwargs.get("boardSize")[1])
		self.elements = []

	#sets elements' positions on the grid
	def updateGrid(self):
		print("updating grid...")
		for element in self.elements:
			self.grid[element.pos] = element.state

	def resolve(self):
		print("resolving state...")

		#spawn new elements
		for element in self.elements:
			if (element.state is State.element1Spawner) or (element.state is State.element2Spawner):
				self.elements.append(element.act_Spawn())

			else:
				element.act_ChangeDirection(Engine.getRandomDirection())
				#move elements
				element.act_Move()

			if self.grid.isOutside(element.pos):
				self.elements.remove(element)


	#increments the game step. computes the next delta t=1step state
	def advance(self):
		print("advancing step...")
		#elements read their environment and propose an action to perform on the next step
		for element in self.elements: element.proposeAction()
		#the game resolves conflicting actions that were proposed by correcting the proposed actions of elements
		#updates elements, they perform their action
		self.resolve()
		#the grid position states are updated for rendering
		self.updateGrid()

	def init(self):
		print("initialising basic game")
		self.elements.append(Element(State.element1Spawner, (0, int(self.grid.y/2)), Direction.right))
		self.elements.append(Element(State.element2Spawner, (self.grid.x-1, int(self.grid.y/2)), Direction.left))
		self.updateGrid()









