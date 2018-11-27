import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep porgram running while flag is active
while True:
#Create Random walk.
    rw = RandomWalk(50000)
    rw.fill_walk()

    #Set the size of window
    plt.figure(dpi=128, figsize= (10, 6))

    #Plot the walk.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s=1)

    #Mark the start and finish
    plt.scatter(0, 0, c = 'green', edgecolor = 'none', s = 10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors = 'none', s = 10)
    
    #Remove Axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    #Draw plot to window
    plt.show()

    keep_running = input("Make another walk?(Y/N)?: ")
    if keep_running == 'n':
        break