from enum import Enum
import random




class State(Enum):
	dead = 0
	element1 = 1
	element2 = 2
	element1Spawner = 3
	element2Spawner = 4
	wall = 5,
	collectible = 6



class Direction():
	none = (0, 0)
	up = (0, 1)
	down = (0, -1)
	left = (-1, 0)
	right = (1, 0)


class Action(Enum):
	nothing = 0

	#movement
	moveUp = 1
	moveDown = 2
	moveLeft = 3
	moveRight = 4

	#actions
	shout = 5
	spawnElement1 = 6
	spawnElement2 = 7





class Grid:

	def __init__(self, X, Y):
		self.board = [[State.dead for y in range(Y)] for x in range(X)] #XxY grid
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

	def isOutside(self, Tuple):
		if 0 > Tuple[0] or Tuple[0] >= self.x or 0 > Tuple[1] or Tuple[1] >= self.y:
			return True
		return False

	#debug function for scrambling the positions
	def scramble(self):
		for block in self.list():
			self[block] = random.choice(list(State))






class Element:
	#intrinsic
	state = State.dead
	health = 0	#block/step
	lifespan = 0
	pos = [] #tuple x, y block

	#actions
	speed = 0	#block per step
	direction = [] #(vertical, horizontal)
				   #(0,0 for nowhere, (1,1) means top left)
	see = 0	#block radius
	speak = 0	#block radius
	hear = 0   #block radius
	hit = 0	#hit per block radius per step

	#proposed action
	proposed_action = []

	def __init__(self, state, pos, direction = (0, 0)):
		self.state = state
		self.pos = pos
		self.direction = direction

	def proposeAction(self):
		if self.state is State.element1Spawner:
			self.proposed_action = Action.spawnElement1

		if self.state is State.element2Spawner:
			self.proposed_action = Action.spawnElement2

	def act_Spawn(self):
		newElementPos = tuple([pos + diri for pos, diri in zip(self.pos, self.direction)])
		if self.state is State.element1Spawner: newElementState = State.element1
		if self.state is State.element2Spawner: newElementState = State.element2
		return Element(newElementState, newElementPos, self.direction)

	def act_ChangeDirection(self, Direction):
		self.direction = Direction

	def act_Move(self):
		self.pos = tuple([pos + diri for pos, diri in zip(self.pos, self.direction)])

	def act_Die(self):
		self.state = State.dead

	#perform the proposed action
	def update(self):
		print("updating")



	#how an element will interact with another element
	def interact(self, Element):
		print("elements iteracted")







