"""Experiment with Matplotlib:
Try changing the colors of a plot.
Add labels to the x-axis and y-axis.
Change the title of the plot.


Write a short paragraph (2-3 sentences) about one interesting
thing you learned from playing around with Matplotlib."""

"""
One intresting thing I learned from playing around with Matplotlib is that 
I can change the colors and fonts of most things, and if you dont give x and y vals
it uses the number of the index to make the visual of the plot which is helpful. 
"""


import matplotlib.pyplot as plt
import numpy as np

yvals = np.array([1, 2, 3, 4])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Title NAAAME", fontdict = font1)
plt.xlabel("NumBERSSS", fontdict = font2)
plt.ylabel("More NUMBErs", fontdict = font2)

plt.plot(yvals, marker = 'o', ms = 10, mfc = 'r')
plt.show()