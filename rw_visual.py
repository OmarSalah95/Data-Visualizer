import matplotlib.pyplot as plt

from random_walk import RandomWalk


#Create and plot a Random walk
rw = RandomWalk()
rw.fill_walk()
#Plot
plt.scatter(rw.x_values, rw.y_values, s=1)
plt.show()