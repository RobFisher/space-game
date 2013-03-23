__author__ = 'rob'


import random
import math
import word_generator


grid_square_size = 1000


class Star(object):
    """A star system."""

    def __init__(self, seed, distance_from_civilisation):
        r = random.Random()
        r.seed(seed)
        name_length_modifier = int(math.sqrt(distance_from_civilisation))
        min_name_length = name_length_modifier + 2
        max_name_length = name_length_modifier + 7
        self.name = word_generator.make_word(r, min_name_length, max_name_length)
        # position within grid square
        self.x = r.randint(0, grid_square_size - 1)
        self.y = r.randint(0, grid_square_size - 1)
