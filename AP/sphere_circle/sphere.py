# matplotlib and numpy

import matplotlib.pyplot as plt
import numpy as np

def plot_sphere(r,x,y):
    z = (abs(r**2 - x**2 - y**2))**0.5
    
    return z,-z
    

xdata = []
ydata = []  
z1data = []    
z2data = []  

r = 100
step = 1

for i in np.arange(-r,r+step,step):
    
    for j in np.arange(-r,r+step,step):
        
        a,b = plot_sphere(r,i,j)
        xdata.append(i)
        ydata.append(j)
        z1data.append(a)
        z2data.append(b)



fig = plt.figure()
f1 = fig.add_subplot(projection='3d')

xdata = np.array(xdata)
ydata = np.array(ydata)
z1data = np.array(z1data)
z2data = np.array(z2data)

# plt.xlim(-12,12)
# plt.ylim(-12,12)
# plt.clim(-12,12)

f1.plot_trisurf(xdata,ydata,z1data)
f1.plot_trisurf(xdata,ydata,z2data)

f1.set_box_aspect((1, 1, 1)) 
# set_box_aspect just scales according to factor like z is scaled 1.9 comapred to x and y
plt.show()