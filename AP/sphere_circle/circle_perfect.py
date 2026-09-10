# matplotlib and numpy

import matplotlib.pyplot as plt
import numpy as np

def plot_circle(r,x):
    y = (abs(r**2 - x**2))**0.5
    
    return y,-y
    
    

# lets take range from -0.9 to 1.1 (original_minima) to 3.1

xcord = []
ycord1 = []  # Top half
ycord2 = []  # Bottom half

r = 10
# CHANGE 1: Range changed from (-80,80) to (-10,11) to match radius 10
for i in np.arange(-r, r + 0.01, 0.01):
    # CHANGE 2: Unpack BOTH return values (y1 and y2)
    y1, y2 = plot_circle(r,i)
    ycord1.append(y1)
    ycord2.append(y2)
    
    xcord.append(i)
    
    
    
# numpy used here
x1 = np.array(xcord)
y1 = np.array(ycord1)
y2 = np.array(ycord2)

# matplotlib usedd from here
# CHANGE 3: Plot upper and lower halves separately
plt.figure(figsize=(6,6))
plt.plot(x1, y1, color='blue')
plt.plot(x1, y2, color='blue')

# plt.gca().set_aspect('equal')  # Keeps circle round, not stretched
plt.grid(True)
plt.xlim(-12,12)
plt.ylim(-12,12)
plt.show()