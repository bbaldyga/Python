import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random wakl, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    #Set the zise of the polting window 
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
    edgecolor='none', s=1)
    #plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk (y/n): ")
    if keep_running == 'n':
        break