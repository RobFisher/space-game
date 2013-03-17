__author__ = 'rob'

import random
import math
from star import Star


base_seed = 'spacegame'
galaxy_radius = 100


class GridSquare(object):
    """A procedurally generated area of the game map."""

    def __init__(self, x, y):
        """Create a grid square at the specified coordinates."""
        self.x = x
        self.y = y
        self.name = 'Sector ' + str(x) + ',' + str(y)
        r = random.Random()
        r.seed(self.name)
        distance_from_centre = math.hypot(x, y)
        self.num_stars = r.randint(1, max(1, galaxy_radius - int(distance_from_centre)))
        self.stars = []
        for i in range(0, self.num_stars):
            star_seed = self.name + '-' + str(i)
            self.stars.append(Star(star_seed))

    def info(self):
        print self.name
        for star in self.stars:
            print star.name + ': ' + str(star.x) + ', ' + str(star.y)
