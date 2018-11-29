from die import Die

import pygal


#Initiate die instance
die_1= Die()
die_2= Die()

#Roll and store restults. 
results = []
for roll in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Convert results to bar graph.
hist = pygal.Bar()

hist.title = "Results of rolling two six sided die 10000 times"
hist.x_labels = range(2, max_result+1)
hist.x_title = "Result"
hist.y_title = "Result Frequency"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')