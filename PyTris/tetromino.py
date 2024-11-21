from config import *

class Tetromino(object):
    rows = 20
    cols = 20
    
    def __init__(self, col, row, shape):
        self.x = col
        self.y = row
        self.shape = shape
        self.color = tetromino_colors[tetrominos.index(shape)]
        self.rotation = 0