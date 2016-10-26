import Globals
import random
import networkx as nx

#unit of space on the board grid. container for elements
#TODO: let elements be independent entities, have value contain a list of entities AND the count. for now only the count to keep things simple. plus its the more abstracted approach

#TODO: look at GraphViz for graph drawing and layout algorithms 

#Note: value is a dict of element types/state keys and element count values
class Block:

	def __init__(self):
		self.state = Globals.BlockState.empty
		self.value = {}

		for state in Globals.ElementState:
			self.value[state] = {}

	#increment the count of the element type in the block
	def __iadd__(self, Elements):
		for element in [Elements]:
			self.value[element.state][id(element)] = element

	def __isub__(self, Elements):
		for element in [Elements]:
			try:
				del self.value[element.state][id(element)]
			except:
				raise ValueError("Cannot delete Element because it does not exist.")
				continue

	#returns the count on the element type
	def __getitem__(self, Element):
		try:
			return self.value[Element.state][id(Element)]
		except:
			raise ValueError("Element does not exist in Block")
			return None

	def setElements(self, Elements):
		self.clear()
		self += Elements

	def clear(self):
		for key, elemtDict in self.value.items():
			elemDict.clear() 

	def has(self, Element):
		if self.value[Element.state][id(Element)]:
			return True
		return False

	def count(self, ElementState):
		return len(self.value[ElementState])

	def dprint(self):
		print("Block ID: ", id(self))
		print("state: ", self.state)
		print("Elements...")
		for elementState, elements in self.value.items():
			print(elementState, self.count())
		print("")

	#these are handled in Engine now
	#a function argument computes the state and sets it
	#WARNING: make sure this can be done right
	#def resolveState(RS_Function):
	#	self.state = RS_Function(self)

	#a function argument computes the value and sets it
	#def resolveElements(RE_Function):
	#	self.value = RE_Function(self)

	#returns bool for if the block has atLeast many ElementStates



class Board:

	def __init__(self, X, Y):
		self.grid = [[Block() for y in range(Y)] for x in range(X)] #XxY grid
		self.x = X
		self.y = Y

	#overload [] operator to pass tuple positions and retrive board positions
	def __getitem__(self, indexTuple):
		answer = self.grid
		for i in indexTuple:
			answer = answer[i]
		return answer

	def __setitem__(self, indexTuple, Elements):
		block = self.grid[indexTuple[0]][indexTuple[1]]
		block = Elements

	#def __iadd__(self, indexTuple, Elements):
	#	self.grid[indexTuple[0]][indexTuple[1]] += Elements
#
#	#def __isub__(self, indexTuple, Elements):
	#	self.grid[indexTuple[0]][indexTuple[1]] -= Elements

	#returns a list of board positions
	def posList(self):
		positions = []
		for x in range(self.x):
			for y in range(self.y):
				positions.append((x, y))
		return positions


	def blockList(self):
		blocks = []
		for pos in self.posList():
			blocks.append(self[pos])
		return blocks

	def isOutside(self, Tuple):
		if 0 > Tuple[0] or Tuple[0] >= self.x or 0 > Tuple[1] or Tuple[1] >= self.y:
			return True
		return False

	#debug function for scrambling the positions
	def scramble(self):
		for pos in self.list():
			self[pos] = random.choice(list(Globals.BlockState))












