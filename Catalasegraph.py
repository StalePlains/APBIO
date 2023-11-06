import matplotlib.pyplot as plt
import numpy as np

# Adding all the necessary data and calculating the margins for percent error to be added to the graph
concentrations = np.array(['0', '0.375', '0.75', '1.5', '3'])

means = np.array([0, 0.0663, 0.1556, 0.2303, 0.4135])
standard_errors = np.array([0, 0.0054, 0.0275, 0.0684, 0.1947])
standard_errors = standard_errors * 2

# Labelling and creating the axes, title, and bars of the graph
plt.xlabel("Concentrations of Hydrogen Peroxide (%)")
plt.ylabel("Mean Rate of Reaction (mol/s)")
plt.title("Concentrations of Hydrogen Peroxide (%) vs Mean Rate of Reaction (mol/s)")
plt.bar(concentrations, means, yerr=standard_errors, color='lightgray', ec='black', capsize=5)
plt.show()

