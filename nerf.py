import numpy as np
import matplotlib.pyplot as plt

angles = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60,70, 80, 90]
distances = [61, 116, 177.3333333, 246, 296.3333333, 539.6666667, 680.3333333, 733.6666667, 651, 652, 534.6666667, 303.6666667, 24.66666667, 0]


result = np.polyfit(angles, distances, 2)
print(result)

equation = np.poly1d(result)
print(equation)
print(equation(2))