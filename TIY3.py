import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    # Make a random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values[1:len(rw.x_values)-1], rw.y_values[1:len(rw.y_values)-1], 'b', linewidth=1)

    # Point out the first and last points.
    ax.plot(0, 0, 'green', linewidth=1)
    ax.plot(rw.x_values[-1], rw.y_values[-1], 'red', linewidth=1)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
