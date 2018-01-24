import pygame, sys, glob, os

pygame.init()

""" -------------- Setting up the screen -------------- """
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))
""" --------------------------------------------------- """

""" -------------- Setting up fps -------------- """
FPS = 60
REFRESH = pygame.USEREVENT + 1
pygame.time.set_timer(REFRESH, 1000 // FPS)
""" -------------------------------------------- """

""" -------------- Setting up the background -------------- """
menuBackground = (0,0,0)
gameBackground = pygame.image.load(os.path.join("images", "gameBackground.jpg"))
""" ------------------------------------------------------- """

""" --------------------------------------------- Player Class --------------------------------------------- """
class player:
	def __init__(self):
		self.x = displayWidth / 2
		self.y = displayHeight / 2
		self.anim = glob.glob(os.path.join("images", "player*.png")) # 0 = down, 1 = left, 2 = right, 3 = up
		self.img = pygame.image.load(self.anim[3])
		self.update(0, 0, "up")

	def update(self, deltaPosX, deltaPosY, direction):

		if deltaPosX != 0 or deltaPosY != 0: # if the player is either moving in the x or y directions

			# ------ Moving the player ----- #
			self.x += deltaPosX
			self.y += deltaPosY
			# ------------------------------ #

			# ------------ Changing direction of player ----------- #
			if direction == "up":
				self.img = pygame.image.load(self.anim[3])
			elif direction == "down":
				self.img = pygame.image.load(self.anim[0])
			elif direction == "left":
				self.img = pygame.image.load(self.anim[1])
			elif direction == "right":
				self.img = pygame.image.load(self.anim[2])
			# ----------------------------------------------------- #

		screen.blit(self.img, (self.x, self.y))
""" -------------------------------------------------------------------------------------------------------- """

""" ---- Global variables ---- """
player = player()
deltaPosX = 0
deltaPosY = 0
direction = "up"
""" -------------------------- """

""" ---------------- Game Loop ---------------- """
def run():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == REFRESH:
				draw()

		player.update(deltaPosX, deltaPosY, direction)
		pygame.display.update()
""" ------------------------------------------- """

""" -------------- Drawing function -------------- """
def draw():
	screen.blit(gameBackground, (0,0))
""" ---------------------------------------------- """

run()
pygame.quit()
sys.exit()