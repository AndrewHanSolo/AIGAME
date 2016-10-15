from enum import Enum




class Pos(Enum):
	empty = 0
	element1 = 1
	element2 = 2


class Grid:

	def __init__(self, N, M):
		self.board = [[Pos.empty]*N for x in range(M)] #NxM grid



class Element:
	#intrinsic
		health = -1	#block/step

	#actions
		move = -1	#block radius
		see = -1	#block radius
		speak = -1	#block radius
		hit = -1	#hit per block radius per step


