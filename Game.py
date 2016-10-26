from Globals import *
import Board
import Element
import Engine
import random
import gc #optional garbage collector

class Game:

	random.seed()
	gc.enable() #enable garbage collection for the game
				#WARNING: dont trust this

	def __init__(self, **kwargs):
		self.board = Board.Board(kwargs.get("boardSize")[0], kwargs.get("boardSize")[1])
		self.engine = Engine.Engine(self.board)

	#sets elements' positions on the board
	def advanceStep(self):
		dprint("updating board...")
		self.engine.advanceStep()
		#self.engine.computeBlocks(self.board)
		#for block in self.board.blockList():
			#pprint (vars(block))
		#	block.dprint()
		#self.board = self.engine.advanceStep(self.board)
		#for element in self.elements:
		#	self.board[element.pos] = element.state
#
	#def resolve(self):
#	#	print("resolving state...")
#
#	#	#spawn new elements
#	#	for element in self.elements:
#	#		if (element.state is State.element1Spawner) or (element.state is State.element2Spawner):
#	#			self.elements.append(element.act_Spawn())
#
#	#		else:
#	#			element.act_ChangeDirection(Engine.getRandomDirection())
#	#			#move elements
#	#			element.act_Move()
#
#	#		if self.board.isOutside(element.pos):
#	#			self.elements.remove(element)
#
#	#	self.engine.computeNextBoard(self.board, [Engine.resolve_Spawner])
#

	#increments the game step. computes the next delta t=1step state
	#def advance(self):
	#	print("advancing step...")
	#	#elements read their environment and propose an action to perform on the next step
	#	for element in self.elements: element.proposeAction()
	#	#the game resolves conflicting actions that were proposed by correcting the proposed actions of elements
	#	#updates elements, they perform their action
	#	self.resolve()
	#	#the board position states are updated for rendering
	#	self.updateBoard()

	def init(self):
		print("initialising basic game")

		#create enemy1spawner at middle leftmost block
		elementSpawner1Pos = (0, int(self.board.y/2))
		elementspawner1 = Element.Element(ElementState.element1Spawner, elementSpawner1Pos, Direction.right)
#
#		##create enemy2spawner at middle rightmost block
		elementSpawner2Pos = (int(self.board.x-1), int(self.board.y/2))
		elementspawner2 = Element.Element(ElementState.element2Spawner, elementSpawner2Pos, Direction.left)

		print(id(elementspawner1))
		self.board[elementSpawner1Pos] += elementspawner1
		self.board[elementSpawner2Pos] += elementspawner2

		#self.updateBoard()
		









