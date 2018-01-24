import pygame, sys

pygame.init()

""" Setting up the screen """
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))

""" Setting up the background """
menuBackground = (0,0,0)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pygame.display.update()
