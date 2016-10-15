import pygame
from Game import *
from Render import *

game_args = {
	
	"boardSize" : [50, 50],
	"windowSize": (600, 600),
	"caption": "AIGAME"




}

pygame.init()
window = pygame.display.set_mode(game_args["windowSize"])
pygame.display.set_caption(game_args["caption"])


game = Game(**game_args)
game.init()

RUNNING = True
while RUNNING:

	for event in pygame.event.get():
		if event == pygame.QUIT:
			RUNNING = False
			pygame.quit()
			sys.exit()

	game.advance()
	render(window, game, **game_args)



sys.exit()
pygame.quit()