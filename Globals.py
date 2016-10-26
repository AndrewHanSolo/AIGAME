from enum import Enum

DEBUG = False

class ElementState(Enum):
	dead = 0
	element1 = 1
	element2 = 2
	element1Spawner = 3
	element2Spawner = 4
	wall = 5,
	collectible = 6

class BlockState(Enum):
	empty = 0
	element1 = 1
	element2 = 2
	element1Spawner = 3
	element2Spawner = 4

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

def dprint(*args):
	if DEBUG:
		for arg in args:
			print(arg)