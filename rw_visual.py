import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep porgram running while flag is active
while True:
#Create Random walk.
    rw = RandomWalk()
    rw.fill_walk()

    #Plot the walk.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s=10)
    plt.show()

    keep_running = input("Make another walk?(Y/N)?: ")
    if keep_running == 'n':
        break