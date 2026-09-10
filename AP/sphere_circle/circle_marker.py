# matplotlib and numpy

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_circle(r,x):
    y = (abs(r**2 - x**2))**0.5
    
    return y,-y
    
    



x_cord = []
y_cord1 = []  # Top half
y_cord2 = []  # Bottom half

r = 10
step = 1

# make step smaller to see smoother circle but range negative r to positive r
for i in np.arange(-r, r + step,step):

    y1, y2 = plot_circle(r,i)
    y_cord1.append(y1)
    y_cord2.append(y2)
    x_cord.append(i)
    

# matplotlib usedd from here
# CHANGE 3: Plot upper and lower halves separately
plt.figure(figsize=(6,6))
plt.plot(x_cord, y_cord1)
plt.plot(x_cord, y_cord2)

# plt.gca().set_aspect('equal')  # Keeps circle round, not stretched
plt.grid(True)
plt.xlim(-12,12)
plt.ylim(-12,12)
plt.show()