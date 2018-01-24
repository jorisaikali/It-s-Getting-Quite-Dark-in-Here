import pygame, sys, glob, os

pygame.init()

""" Setting up the screen """
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))

""" Setting up the background """
menuBackground = (255,255,255) # temporary until states implemented
gameBackground = pygame.image.load(os.path.join("images", "gameBackground.jpg"))

class player:
	def __init__(self):
		self.x = displayWidth / 2
		self.y = displayHeight / 2
		self.anim = glob.glob(os.path.join("images", "player*.png")) # 0 = down, 1 = left, 2 = right, 3 = up
		self.img = pygame.image.load(self.anim[3])
		self.update(0, 0, "up")

	def update(self, deltaPosX, deltaPosY, direction):
		if deltaPosX != 0 or deltaPosY != 0:
			self.x += deltaPosX
			self.y += deltaPosY

			if direction == "up":
				self.img = pygame.image.load(self.anim[3])
			elif direction == "down":
				self.img = pygame.image.load(self.anim[0])
			elif direction == "left":
				self.img = pygame.image.load(self.anim[1])
			elif direction == "right":
				self.img = pygame.image.load(self.anim[2])

		screen.blit(self.img, (self.x, self.y))

player = player()
deltaPosX = 0
deltaPosY = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pygame.display.update()
