import numpy as np

# Names and 2D array of steps
names = ["BigtT", "Tinsley", "King"]
steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

# Print rows, totals, and averages
for i in range(len(names)):
    total = np.sum(steps[i])
    average = np.mean(steps[i])
    print(names[i], "Steps:", steps[i])
    print("Total:", total)
    print("Average:", average)
    print()
    print("Maximum steps in dataset:", np.max(steps))
    print("Minimum steps in dataset:", np.min(steps))

# Reflection
Using a 2D array made it easier to organize the step data for each person in rows. 
It allowed me to calculate totals and averages quickly using NumPy functions. 
Finding the maximum and minimum values was simple because the array stores all data together. 
Overall, arrays made summarizing the dataset faster and more organized.
