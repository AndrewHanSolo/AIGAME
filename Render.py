#Render functions

import pygame
from Grid import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 100, 50)




def render(Screen, Game, **kwargs):

	ws = kwargs.get("windowSize")
	bs = kwargs.get("boardSize")

	#scale factor. 
	#todo: radius scale factor needs to be set
	sf = (ws[0] / bs[0], ws[1] / bs[1])

	Screen.fill(WHITE)

	#blocks = Game.grid.list()
	for block in Game.grid.list():

		blockCoords = tuple([int(i*j)+5 for i, j in zip(block, sf)])

		if Game.grid[block] is Pos.empty:
			pygame.draw.circle(Screen, WHITE, blockCoords, 5, 0)
			continue

		if Game.grid[block] is Pos.element1:
			pygame.draw.circle(Screen, RED, blockCoords, 5, 0)
			continue

		if Game.grid[block] is Pos.element2:
			pygame.draw.circle(Screen, BLUE, blockCoords, 5, 0)
			continue

		if Game.grid[block] is Pos.element1Spawner:
			pygame.draw.circle(Screen, YELLOW, blockCoords, 5, 0)
			continue

		if Game.grid[block] is Pos.element2Spawner:
			pygame.draw.circle(Screen, YELLOW, blockCoords, 5, 0)


	pygame.display.update()

	
		
		


	