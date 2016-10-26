#Render functions
from Globals import *
from Board import *
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 50, 50)
GREY = (50, 50, 50)
GREEN = (0, 255, 0)

StateColor = {
	BlockState.empty: BLACK,
	BlockState.element1: RED,
	BlockState.element2: BLUE,
	BlockState.element1Spawner: GREEN,
	BlockState.element2Spawner: GREEN,
	#BlockState.State.wall: BLACK,
	#BlockState.State.collectible: GREY 
}


def draw(Screen, Game, **kwargs):

	ws = kwargs.get("windowSize")
	bs = kwargs.get("boardSize")

	#scale factor. 
	#todo: radius scale factor needs to be set
	sf = (ws[0] / bs[0], ws[1] / bs[1])

	Screen.fill(WHITE)

	#blocks = Game.grid.list()
	for pos, block in zip(Game.board.posList(), Game.board.blockList()):
		blockCoords = tuple([int(i*j)+5 for i, j in zip(pos, sf)])

		pygame.draw.circle(Screen, StateColor[block.state], blockCoords, 5, 0)

	pygame.display.update()

	
		
		


	