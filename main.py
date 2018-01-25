import pygame, sys, glob, os

pygame.init()

""" -------------- Setting up the screen -------------- """
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))
""" --------------------------------------------------- """

""" -------------- Setting up fps and clock -------------- """
FPS = 120
REFRESH = pygame.USEREVENT + 1
pygame.time.set_timer(REFRESH, 1000 // FPS)

clock = pygame.time.Clock()
""" ------------------------------------------------------ """

""" -------------- Setting up the background -------------- """
menuBackground = (0,0,0)
gameBackground = pygame.image.load(os.path.join("images", "gameBackground.jpg"))
""" ------------------------------------------------------- """

""" --------------------------------------------- Player Class --------------------------------------------- """
class player:
	def __init__(self):
		self.anim = glob.glob(os.path.join("images", "player*.png")) # 0 = down, 1 = left, 2 = right, 3 = up
		self.img = pygame.image.load(self.anim[3])
		self.imgRect = self.img.get_rect()
		self.x = displayWidth // 2 - self.imgRect.width // 2
		self.y = displayHeight // 2 - self.imgRect.height // 2
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

		self.imgRect = self.img.get_rect()
		screen.blit(self.img, (self.x, self.y))
""" -------------------------------------------------------------------------------------------------------- """

""" ---------------- Game Loop ---------------- """
def run():
	deltaPosX = 0
	deltaPosY = 0
	direction = "up"

	while True:
		#for event in pygame.event.get():
		event = pygame.event.wait()

		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == REFRESH:
			draw()

		if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			deltaPosX = 0
			deltaPosY = -3
			direction = "up"
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			deltaPosX = 0
			deltaPosY = 3
			direction = "down"
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			deltaPosX = -3
			deltaPosY = 0
			direction = "left"
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
			deltaPosX = 3
			deltaPosY = 0
			direction = "right"

		limitBorders()

		player.update(deltaPosX, deltaPosY, direction)
		pygame.display.update()
""" ------------------------------------------- """

""" -------------- Drawing function -------------- """
def draw():
	screen.blit(gameBackground, (0,0))
""" ---------------------------------------------- """

""" ------------ Limiting border function ------------"""
def limitBorders():
	# ---------- Limiting upper border ---------- #
	if player.y <= 54:
		player.y = 54
	# ------------------------------------------- #

	# ---------- Limiting lower border ---------- #
	if player.y >= 544 - player.imgRect.height:
		player.y = 544 - player.imgRect.height
	# ------------------------------------------- #

	# ----------- Limiting left border ---------- #
	if player.x <= 53:
		player.x = 53
	# ------------------------------------------- #

	# ---------- Limiting right border ---------- #
	if player.x >= 744 - player.imgRect.width:
		player.x = 744 - player.imgRect.width
	# ------------------------------------------- #
""" ------------------------------------------------ """

player = player()
run()
pygame.quit()
sys.exit()