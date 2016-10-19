from Globals import *
import Board
import Element
import Engine
import random

class Game:

	def __init__(self, **kwargs):
		self.board = Board.Board(kwargs.get("boardSize")[0], kwargs.get("boardSize")[1])
		self.elements = []
		self.engine = Engine.Engine()

	#sets elements' positions on the board
	def updateBoard(self):
		print("updating board...")
		self.engine.computeNextBoard(self.board)
		#for element in self.elements:
		#	self.board[element.pos] = element.state

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

			if self.board.isOutside(element.pos):
				self.elements.remove(element)

		self.engine.computeNextBoard(self.board, [Engine.resolve_Spawner])


	#increments the game step. computes the next delta t=1step state
	def advance(self):
		print("advancing step...")
		#elements read their environment and propose an action to perform on the next step
		for element in self.elements: element.proposeAction()
		#the game resolves conflicting actions that were proposed by correcting the proposed actions of elements
		#updates elements, they perform their action
		self.resolve()
		#the board position states are updated for rendering
		self.updateBoard()

	def init(self):
		print("initialising basic game")
		self.board[(Element.Element(State.element1Spawner, (0, int(self.board.y/2)), Direction.right))
		self.elements.append(Element.Element(State.element2Spawner, (self.board.x-1, int(self.board.y/2)), Direction.left))
		self.updateBoard()









