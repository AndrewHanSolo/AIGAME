#Render functions

import pygame
from Grid import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 50, 50)
GREY = (50, 50, 50)




def render(Screen, Game, **kwargs):

	ws = kwargs.get("windowSize")
	bs = kwargs.get("boardSize")

	#scale factor. 
	#todo: radius scale factor needs to be set
	sf = (ws[0] / bs[0], ws[1] / bs[1])

	Screen.fill(WHITE)

	#blocks = Game.grid.list()
	for element in Game.elements:

		blockCoords = tuple([int(i*j)+5 for i, j in zip(element.pos, sf)])

		if element.state is State.dead:
			pygame.draw.circle(Screen, WHITE, blockCoords, 5, 0)
			continue

		if element.state is State.element1:
			pygame.draw.circle(Screen, RED, blockCoords, 5, 0)
			continue

		if element.state is State.element2:
			pygame.draw.circle(Screen, BLUE, blockCoords, 5, 0)
			continue

		if element.state is State.element1Spawner:
			pygame.draw.circle(Screen, YELLOW, blockCoords, 5, 0)
			continue

		if element.state is State.element2Spawner:
			pygame.draw.circle(Screen, YELLOW, blockCoords, 5, 0)

		if element.state is State.wall:
			pygame.draw.circle(Screen, BLACK, blockCoords, 5, 0)	

		if element.state is State.collectible:
			pygame.draw.circle(Screen, GREY, blockCoords, 5, 0)	


	pygame.display.update()

	
		
		


	