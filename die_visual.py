from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6

die = Die()  # Creating a six sided die

# Make rolls and store the results in a list.
results = []
for roll_num in range(1000):
    results.append(die.roll())

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequencies.append(results.count(value))


# Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(title="Results of Rolling one 6 sided dice 1000 times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename="d6.html")
