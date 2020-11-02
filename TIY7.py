from plotly.graph_objs import Bar, Layout
from plotly import offline

from random import randint


class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


# Create a D6

die_1 = Die(6)  # Creating a six sided die
die_2 = Die(6)
die_3 = Die(6)

# Make rolls and store the results in a list.
results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll() + die_3.roll())

# Analyze the results.
frequencies = []
for value in range(3, die_1.num_sides+die_2.num_sides+die_3.num_sides+1):
    frequencies.append(results.count(value))


# Visualize the results.
x_values = list(range(3, die_1.num_sides+die_2.num_sides+die_3.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", 'dtick': 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(title="Results of Rolling three 6 sided die a total of 1000 times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename="d6_d6_d6.html")
