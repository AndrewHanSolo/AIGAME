import random
import Board

random.seed(0)

def getRandomDirection():
	return (random.randint(-1, 1), random.randint(-1, 1))


#BLOCK RESOLUTION FUNCTIONS

#kill all blocks that arent the spawner
def resolve_Spawner(Block):
	if Block.contains(State.spawner):
		Block.union(State.spawner)




#manages 
class Engine:

	def __init__(self, **kwargs):
		self.id = "prototype"
		self.functions = [
				resolve_Spawner
			] #dict of rules for the game physics

	#performs function on Block in Grid that returns the new state of the Block
	def computeBlock(self, Block, Function):
		return Function(Block)

	#computes each block for entire board and stores in a new board to return
	def computeNextBoard(self, tBoard):
		newBoard = Board.Board(tBoard.x, tBoard.y)
		for Function in self.functions:
			for Block in tBoard.list():
				newBoard[Block] = self.computeBlock(Block, Function)

		return newBoard





