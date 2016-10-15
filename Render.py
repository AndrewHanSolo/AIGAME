#Render functions

import pygame

def render(Game, **kwargs):
	if "caption" in kwargs: pygame.display.set_caption("%s", kwargs.get("caption"))
	if "windowSize" in kwargs: pygame.display.set_mode(kwargs.get("windowSize")[0], kwargs.get("windowSize")[1], 0, 32)

	window.fill(BLACK)
	#for zip(x, y) in Game.grid:
	

	for x in range(len(Game.grid)):
		for y in range(len(Game.grid)):

			if Game.grid[x][y] is Pos.empty:
					pygame.draw.circle(window, WHITE, x, y, DEFAULT_RADIUS, 0)

			if Game.grid[x][y] is Pos.element1:
				pygame.draw.circle(window, RED, x, y, DEFAULT_RADIUS, 0)

			if Game.grid[x][y] is Pos.element2:
				pygame.draw.circle(window, BLUE, x, y, DEFAULT_RADIUS, 0)
	
		
		
		


	