# vary the theta from 0 -> 2pi and plot y as cos(theta) and x as sin(theta)
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd


step = 0.1
x = []
y= []
z = []


for phi in np.arange(-round(0.5*np.pi,6),round(0.5*np.pi,6)+step,step):
    for i in np.arange(0,round(2*np.pi,6)+step,step):
        x.append(np.sin(i)*np.cos(phi)) 
        y.append(np.cos(i)*np.cos(phi)) # -1 min radius of circle 0 max radius of circle +1 again min radius of circle
        z.append(np.sin(phi)) # from -1 to +1 height
        


# In[28]:


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot3D(x,y,z)
# ax.set_box_aspect((1,1,1))
ax.set_box_aspect((1,1,1))
plt.xlabel("x")
plt.ylabel("y")

plt.show()



