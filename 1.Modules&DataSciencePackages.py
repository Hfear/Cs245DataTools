
"""Imports NumPy, pandas, and Matplotlib.
Uses NumPy to create a list of 10 random numbers.
Prints the mean and sum of these numbers using NumPy functions.
Uses Matplotlib to plot a simple line graph of these numbers."""

"""
how do i use it like this??
from numpy.random import *
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#x = random.randint(100, size=(10))
randnums = np.random.randint(100, size=(10))

print(randnums)
print("mean = ", randnums.mean())
print("sum = ", randnums.sum())

randplots = np.array(randnums)

plt.plot(randplots)
plt.show()
