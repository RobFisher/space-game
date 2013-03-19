__author__ = 'rob'


import random
import word_generator


grid_square_size = 1000


class Star(object):
    """A star system."""

    def __init__(self, seed):
        r = random.Random()
        r.seed(seed)
        self.name = word_generator.make_word(r)
        # position within grid square
        self.x = r.randint(0, grid_square_size - 1)
        self.y = r.randint(0, grid_square_size - 1)
