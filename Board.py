from Globals import *
import random

class Block:

	def __init__(self, PosTuple, State, Elements):
		self.pos = PosTuple
		self.state = State
		self.elements = Elements

	def setState(self, state):
		self.state = state

	def setElements(self):
		return self.element

	def contains(self, State):
		for element in self.elements:
			if element.state is State:
				return True
		return False

	#delete elements that are not in list of States
	def union(self, States):
		for state in list(States):
			for element in self.elements:
				if element.state is not state:
					self.elements.remove(element)

	def update(self):
		for element in self.elements:
			element.pos = self.pos
			if element.state is State.dead:
				self.elements.remove(element)



class Board:

	def __init__(self, X, Y):
		self.grid = [[Block(State.dead, {}) for y in range(Y)] for x in range(X)] #XxY grid
		self.x = X
		self.y = Y

	#overload [] operator to pass tuple positions and retrive board positions
	def __getitem__(self, indexTuple):
		answer = self.grid
		for i in indexTuple:
			answer = answer[i]
		return answer

	#overload set operator, position tuple access board position and sets value
	def __setitem__(self, key, value):
		self.grid[key[0]][key[1]].value

	#helper function for returning a list tuples of all board positions
	def list(self):
		positions = []
		count = 0
		for x in range(self.x):
			for y in range(self.y):
				positions.append((x, y))
				count+=1
		#print(count)
		return positions

	def isOutside(self, Tuple):
		if 0 > Tuple[0] or Tuple[0] >= self.x or 0 > Tuple[1] or Tuple[1] >= self.y:
			return True
		return False

	#debug function for scrambling the positions
	def scramble(self):
		for pos in self.list():
			self[pos] = random.choice(list(State))












