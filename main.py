# Ian Fletcher
# CST-305
# 2/22/2023
# Green's Function Code

# imports necessary libraries
import numpy as np
from matplotlib import pyplot as plt
import math


# result for homogenous equation of part 1
def h1_equation(x):
    return (-3/4) * pow(math.e, -2*x)


# result for Green's function equation of part 1
def g1_equation(t):
    return ((1/2) * pow(t, 2)) - ((3/2) * t) + (3/4) - ((3/4) * (pow(math.e, -2*t)))


# result for homogenous equation of part 2
def h2_equation(x):
    return 4 * math.cos(x)


# result for Green's function equation of part 2
def g2_equation(t):
    return 4 - 4 * math.cos(t)


# creates empty arrays for y values
h1_y = []
g1_y = []
h2_y = []
g2_y = []

# populates arrays with first 100 values from equations
for i in range(100):
    h1_y.append(h1_equation(i))
    g1_y.append(g1_equation(i))
    h2_y.append(h2_equation(i))
    g2_y.append(g2_equation(i))

# uses linspace to generate x values
x = np.linspace(1, 100, 100)

# plots the homogenous equation of part 1
plt.plot(x, h1_y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Homogenous Equation 1")
plt.show()
# plots the Green's function result of part 1
plt.plot(x, g1_y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Green's Function 1")
plt.show()
# plots the homogenous equation of part 2
plt.plot(x, h2_y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Homogenous Equation 2")
plt.show()
# plots the Green's function result of part 2
plt.plot(x, g2_y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Green's Function 2")
plt.show()

