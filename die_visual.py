from die import Die

# Create a D6

die = Die()  # Creating a six sided die

# Make rolls and store the results in a list.
results = []
for roll_num in range(100):
    results.append(die.roll())

print(results)
