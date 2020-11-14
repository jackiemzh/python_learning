import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

plt.plot(np_baseball[:,0], np_baseball[:,1])

plt.show()



# scatter plot  --------------------------
plt.scatter(np_baseball[:,0], np_baseball[:,1])

# Put the x-axis on a logarithmic scale
plt.xscale("log")

# Show plot
plt.show()


# Basic scatter plot, log scale
dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}

plt.scatter(gdp_cap, life_exp, c=col, alpha=0.8)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)


# Add title
plt.title(title)

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks([1000,10000,100000],
['1k','10k','100k'])


# Additional customizations ------ highlight the points
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')


# Add grid() call
plt.grid(True)


# After customizing, display the plot
plt.show()


# Build histogram with 5 bin  --------------------------
plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins=20)


# Show and clean up again
plt.show()
plt.clf()



