import matplotlib.pyplot as plt
import numpy as np

concentrations = np.array(['0', '0.375', '0.75', '1.5', '3'])

means = np.array([0, 0.0663, 0.1556, 0.2303, 0.4135])
standard_errors = np.array([0, 0.0054, 0.0275, 0.0684, 0.1947])
standard_errors = standard_errors * 2

print(standard_errors)

plt.xlabel("Mean Concentrations of Hydrogen Peroxide (%)")
plt.ylabel("Rate of Reaction (mol/s)")
plt.title("Mean Concentrations of Hydrogen Peroxide (%) vs Rate of Reaction (mol/s)")
plt.bar(concentrations, means, yerr=standard_errors, color='lightgray', ec='black', capsize=5)
plt.show()

