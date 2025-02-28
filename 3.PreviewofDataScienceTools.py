"""Task:
Import NumPy, pandas, and Matplotlib.
Perform the following simple operations:
Use NumPy to create an array of 5 random numbers and print them.
Use pandas to create a simple table with 3 columns (Name, Age, City) and 3 rows.
Use Matplotlib to create a basic bar chart with 3 bars (representing any made-up values).
Example Output:
A list of 5 random numbers.
A small table displayed in pandas.
A bar chart with 3 bars."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

randnums = np.random.randint(10, size=(5))
print(randnums)

data = {
    "Name": ["Hannah", "anna", "nn"],
    "Age": [22, 11, 00],
    "City": ["NY", "switxerland", "jersey"]
}

table = pd.DataFrame(data)

print(table)

x = np.array(["1", "2", "3"])
y = np.array([1, 2, 3])

plt.bar(x, y, color = "hotpink")
plt.show()


