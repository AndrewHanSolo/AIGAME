import pygame
from Game import *
from Render import *
import time

game_args = {
	
	"boardSize" : [50, 50],
	"windowSize": (600, 600),
	"caption": "AIGAME",
	"renderSpeed": 0.1




}

pygame.init()
window = pygame.display.set_mode(game_args["windowSize"])
pygame.display.set_caption(game_args["caption"])


game = Game(**game_args)
game.init()

RUNNING = True
while RUNNING:

	start_time = time.time()

	for event in pygame.event.get():
		if event == pygame.QUIT:
			RUNNING = False
			pygame.quit()
			sys.exit()

	game.advance()
	draw(window, game, **game_args)

	end_time = time.time()
	elapsed_time = end_time - start_time
	print(elapsed_time, type(elapsed_time))
	time.sleep(game_args["renderSpeed"] - elapsed_time)



sys.exit()
pygame.quit()