from Globals import *
import random
import Board

random.seed(0)

def getRandomDirection():
	return (random.randint(-1, 1), random.randint(-1, 1))


#BLOCK RESOLUTION FUNCTIONS

####
#### Resolve Block State Functions (also resolves value)
####

#kill all blocks that arent the spawner
def RS_resolve_spawner(Block):
	if Block.count(ElementState.element1Spawner) or Block.count(ElementState.element2Spawner):
		Block.state = BlockState.element1Spawner
	return Block

def RS_random_state(Block):
	Block.state = random.choice(list(BlockState))
	return Block


#WORLD RESOLUTION FUNCTIONS
def RB_do_nothing(Board):
	return Board





#computes block and world physics, handles event stack
class Engine:

	def __init__(self, Board, **kwargs):
		self.id = "prototype"
		self.RS_Functions = [
				RS_resolve_spawner,
				RS_random_state
			] #dict of rules for the game physics

		self.RB_Functions = [
			RB_do_nothing
		]

		self.tBoard = Board


	#performs function on Block in Grid that returns the new state of the Block
	def computeBlock(self, Block, B_Function):
		return B_Function(Block)

	#computes each block for entire board and stores in a new board to return
	def computeBlocks(self):
		for Function in self.RS_Functions:
			for pos, Block in zip(self.tBoard.posList(), self.tBoard.blockList()):
				self.computeBlock(self.tBoard[pos], Function)

	def computeWorld(self):
		for Function in self.RB_Functions:
			self.tBoard = Function(self.tBoard)

	def advanceStep(self):
		self.computeBlocks()
		self.computeWorld()
		#tBoard = self.computeBlocks(tBoard)
		#tBoard = self.computeWorld(tBoard)



#class Renderer:
#
#	def __init__(self, **kwargs):
#		self.id = "prototype"
#		self.DB_Functions = {
#			Globals.State.Element: DB_ElementSpawner
#		}
#
		






