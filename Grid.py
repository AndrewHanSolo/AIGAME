from enum import Enum
import random




class Pos(Enum):
	empty = 0
	element1 = 1
	element2 = 2
	element1Spawner = 3
	element2Spawner = 4


class Grid:

	def __init__(self, X, Y):
		self.board = [[Pos.empty for y in range(Y)] for x in range(X)] #XxY grid
		self.x = X
		self.y = Y

	#overload [] operator to pass tuple positions and retrive board positions
	def __getitem__(self, indexTuple):
		answer = self.board
		for i in indexTuple:
			answer = answer[i]
		return answer

	#overload set operator, position tuple access board position and sets value
	def __setitem__(self, key, value):
		self.board[key[0]][key[1]] = value

	#helper function for returning a list tuples of all board positions
	def list(self):
		blocks = []
		count = 0
		for x in range(self.x):
			for y in range(self.y):
				blocks.append((x, y))
				count+=1
		#print(count)
		return blocks

	#debug function for scrambling the positions
	def scramble(self):
		for block in self.list():
			self[block] = random.choice(list(Pos))






class Element:
	#intrinsic
	state = Pos.empty
	health = -1	#block/step
	lifespan = -1
	pos = [] #tuple x, y block

	#actions
	speed = -1	#block per step
	direction = -1 #(vertical, horizontal)
				   #(0,0 for nowhere, (1,1) means top left)
	see = -1	#block radius
	speak = -1	#block radius
	hear = -1   #block radius
	hit = -1	#hit per block radius per step

	#proposed action
	proposed_action = []

	def __init__(self, state, pos):
		self.state = state
		self.pos = pos

	def proposeAction(self):
		print("proposing action for next step")
		proposed_action = []

	#how an element will interact with another element
	def interact(self, Element):
		print("elements iteracted")







