import pygal
from die import Die

#Create D6
die = Die()

# Make some rolls and store it
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analize the results
frequencies = []
for val in range(1,die.num_sides+1):
    frequency = results.count(val)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling one d6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist._x_title = "Results"
hist._y_title = "Frequency of Results"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')