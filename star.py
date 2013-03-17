__author__ = 'rob'


import random


grid_square_size = 1000


class Star(object):
    """A star system."""

    def __init__(self, seed):
        r = random.Random()
        r.seed(seed)
        name_length = r.randint(3, 20)
        self.name = ''
        for i in range(0, name_length):
            self.name += chr(ord('a') + r.randint(0,25))
        # position within grid square
        self.x = r.randint(0, grid_square_size - 1)
        self.y = r.randint(0, grid_square_size - 1)
