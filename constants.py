# Screen Size
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500

# Game Settings
SPEED = 5
PLAYER_SIZE, WALL_SIZE = SPEED, 15
STARTDIST, TELEDIST = 15, 50
STARTPOS = (
    (STARTDIST + WALL_SIZE, STARTDIST + WALL_SIZE),
    (
        SCREEN_WIDTH - STARTDIST - PLAYER_SIZE - WALL_SIZE,
        SCREEN_HEIGHT - STARTDIST - PLAYER_SIZE - WALL_SIZE,
    ),
)

# Network Settings
MAX_PLAYERS = 2
QUEUE_SIZE = 2
PORT = 5675

# Client Properties
OFFLINE, WAITING, INGAME, WIN, LOSE = 0, 1, 2, 3, 4
PLAYER1, PLAYER2 = 0, 1
MAX_TELEPORTS = 3

# Colors
BLUE, GREEN, RED, BLACK, WHITE = (
    (0, 0, 255),
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 0),
    (255, 255, 255),
)

# Index Constants
X, Y = 0, 1
STATE = 0

# Timer Constants
WAITING_ANIMATION_TIMER = 30
END_SCREEN_TIMER = 150

# Font Size
FONT_SIZE = 50
