from Globals import *

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

