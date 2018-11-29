from die import Die

import pygal


#Initiate die instance
die = Die()

#Roll and store restults. 
results = []
for roll in range(10000):
    result = die.roll()
    results.append(result)

#Analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Convert results to bar graph.
hist = pygal.Bar()

hist.title = "Results of rolling one six sided die 10000 times"
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = "Result"
hist.y_title = "Result Frequency"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')