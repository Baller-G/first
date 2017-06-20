import numpy as np
import matplotlib.pyplot as plt

angles = [-40, -20, 0, 20, 40, 60, 80]
distances = [61, 177.33, 296.33, 680.33, 651, 534.67, 24.67]

result = np.polyfit(angles, distances, 4)
print(result)

equation = np.poly1d(result)
print(equation)

while True:
    angle = int(raw_input("What angle do you choose?"))
    print(equation(angle))