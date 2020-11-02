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


print(frequencies)
