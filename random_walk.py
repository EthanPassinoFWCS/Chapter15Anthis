from random import choice
class RandomWalk:

    def __init__(self, num_points=5000):
        self.num_poins = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
