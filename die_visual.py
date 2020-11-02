from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6

die_1 = Die()  # Creating a six sided die
die_2 = Die(10)

# Make rolls and store the results in a list.
results = []
for roll_num in range(50000):
    results.append(die_1.roll() + die_2.roll())

# Analyze the results.
frequencies = []
for value in range(2, die_1.num_sides+die_2.num_sides+1):
    frequencies.append(results.count(value))


# Visualize the results.
x_values = list(range(2, die_1.num_sides+die_2.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", 'dtick': 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(title="Results of Rolling one 6 sided dice, one 10 sided dice, a total of 50000 times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename="d6_d10.html")
