import plotly.express as px
import matplotlib.pyplot as plt
from random import randint, choice


class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


class RandomWalk:

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # Calc new pos
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice(range(0, 5))  # range of 0-4
        return direction * distance


def create_die_roll_vis():
    die_1 = Die()  # Creating a six sided die
    die_2 = Die()

    # Make rolls and store the results in a list.
    results = [die_1.roll() + die_2.roll() for x in range(1000)]  # List comprehensions.

    # Analyze the results.
    frequencies = [results.count(x) for x in range(2, die_1.num_sides+die_2.num_sides+1)]  # List comprehensions.

    # Visualize the results.
    x_values = [x for x in range(2, die_1.num_sides+die_2.num_sides+1)]  # List comprehensions.

    plt.bar(x_values, frequencies, color='maroon', width=0.4)

    plt.xlabel("Number Rolled")
    plt.ylabel("Times Number Rolled")
    plt.title("Two six sided dice rolled 1000 times result")
    plt.show()

def create_rw_vis():
    rw = RandomWalk()
    rw.fill_walk()

    fig = px.scatter(rw.x_values, rw.y_values)
    fig.show()


create_rw_vis()
create_die_roll_vis()
