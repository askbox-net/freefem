import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
# read data
coord = pd.read_csv('outputs/u.csv',header=None).values
x = coord[:,0]
y = coord[:,1]
z = coord[:,2]
tridata = pd.read_csv('outputs/Th.csv',header=None).values
tri = mtri.Triangulation(x,y,triangles=tridata)

# plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_trisurf(tri,z,cmap=plt.cm.jet)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u')
plt.savefig('outputs/python.eps')
plt.show()

