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

def RB_set_nodes(Board):
	centerPos = int(Board.x/2), int(Board.y/2)
	for block in Board.blockList(centerPos, 10):
		block.state = BlockState.alive



def RB_game_of_life(Board):

	#for every block on the board
	for pos, block in zip(Board.posList(), Board.blockList()):

		#count how many surrounding blocks are in a state
		surroundingBlocksOn = 0
		for block in Board.blockList(pos, 1):
			if block.state is BlockState.alive: surroundingBlocksOn+=1

		#cases of the counts
		if surroundingBlocksOn == 2 or surroundingBlocksOn == 3:
			block.state = BlockState.alive
		else:
			block.state = BlockState.dead







			






#computes block and world physics, handles event stack
class Engine:

	def __init__(self, Board, **kwargs):
		self.id = "prototype"
		self.RS_Functions = [
				#RS_resolve_spawner,
				RS_random_state
			] #dict of rules for the game physics

		self.RB_Functions = [
			RB_do_nothing,
			RB_game_of_life,
			RB_set_nodes
		]

		self.tBoard = Board

	#def computeElement(self, Element, EA_Function):
	#	return EA_Function(Element)
#
#	#def computeElements(self):
#	#	for Function in self.EA_Functions:
	#		for element in 

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
			Function(self.tBoard)

	#def proposeElementActions()

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
		






