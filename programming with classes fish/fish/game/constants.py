import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_SHELL = os.path.join(os.getcwd(), "/Users/sierradavenport/Downloads/programming with classes fish/fish/assets/shell.png")
IMAGE_OCEAN = os.path.join(os.getcwd(), "/Users/sierradavenport/Downloads/programming with classes fish/fish/assets/ocean.png")
IMAGE_FOOD = os.path.join(os.getcwd(), "/Users/sierradavenport/Downloads/programming with classes fish/fish/assets/food.png")

IMAGE_SHARK = os.path.join(os.getcwd(), "/Users/sierradavenport/Downloads/programming with classes fish/fish/assets/shark.png")


IMAGE_END = os.path.join(os.getcwd(), "/Users/sierradavenport/Downloads/programming with classes fish/fish/assets/end_screen.png")
IMAGE_FISH = os.path.join(os.getcwd(), "/Users/sierradavenport/Downloads/programming with classes fish/fish/assets/fish.png")

SOUND_START = os.path.join(os.getcwd(), "/Users/sierradavenport/Downloads/programming with classes fish/fish/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "/Users/sierradavenport/Downloads/programming with classes fish/fish/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "/Users/sierradavenport/Downloads/programming with classes fish/fish/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

SHELL_WIDTH = 48
SHELL_HEIGHT = 24
# BRICK_SPACE = 5

# PADDLE_SPEED = 5
# PADDLE_WIDTH = 96
# PADDLE_HEIGHT = 24

BALL_WIDTH = 24
BALL_HEIGHT = 24

CLOUD_WIDTH = 200
CLOUD_H = 145

SHARK_WIDTH = 221
SHARK_H = 92

FISH_SPEED = 8
FISH_WIDTH = 115
FISH_HEIGHT = 65

FOOD_H = 20
FOOD_W = 20