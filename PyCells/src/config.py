# cell logic constants
PLACEHOLDER = -1
SAND = 1
WATER = 2
ROCK = 3
BLANK = 11

# cell name constants
names = {
    BLANK: "BLANK",
    SAND: "SAND",
    WATER: "WATER",
    ROCK: "ROCK"
}

# cell matrix constants
window = 0.5  # scalar
m = int(128 * window)  # columns
n = int(256 * window)  # rows
scale = 5  # pixels per cell

max_frame_rate = 60

spread = 1


def set_spread(s):
    global spread
    spread = s


def get_spread():
    return spread


render_optimization = True

SPAWN_CHANCE = 0.5

ROCK_AUX_LIMIT = 2
ROCK_PRIME_LIMIT = 2

unconserved = {BLANK}
def set_unconserved(list_cells):
    for x in list_cells:
        unconserved.add(x)

FLUIDS = {WATER}
viscosity = {
    WATER: 1
}

density = {
    WATER: 1
}

SPLASH_CHANCE = {
    WATER: 0.2
}

colors = {
    BLANK: [(0, 0, 0)],
    SAND: [(245, 215, 175), (240, 210, 170), (235, 200, 160), (230, 195, 150), (225, 190, 150)],
    WATER: [(0, 100, 250)],
    ROCK: [(200, 200, 200), (125, 125, 125), (150, 150, 150)]
}

CONTROLS = {
    "q": BLANK,
    "e": SAND,
    "w": WATER,
    "r": ROCK
}

FPS = 60