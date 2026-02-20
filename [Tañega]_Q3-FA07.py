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
