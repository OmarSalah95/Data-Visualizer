from die import Die


#Initiate die instance
die = Die()

#Roll and store restults. 
results = []
for roll in range(1000):
    result = die.roll()
    results.append(result)

#Analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print (frequencies)

