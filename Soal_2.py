import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# x - 2y + z = 6
# 3x + y - 2z = 4
# 7x - 6y - z = 10
eq1 = [1, -2, 1]
eq2 = [3, 1, -2]
eq3 = [7, -6, -1]
a = np.array([eq1, eq2, eq3])
b = np.array([6, 4, 10])

hasil = np.linalg.solve(a,b)
print(' Nilai x =', hasil[0],'\n','Nilai y =', hasil[1], '\n','Nilai z =', hasil[2])

fig = plt.figure('3D Plotting')
fig.set_figheight(5)
fig.set_figwidth(12)


ax = fig.add_subplot(131, projection='3d')
x = np.array([6,0,0])
y = np.array([0,-3,0])
z = np.array([0,0,6])
ax.plot_trisurf(x,y,z, color='red', alpha=0.4)
ax.scatter(x,y,z)
ax.set_xlabel('Nilai X')
ax.set_ylabel('Nilai Y')
ax.set_zlabel('Nilai Z')
ax.set_title('x - 2y + z = 6')


bx = fig.add_subplot(132, projection='3d')
x1 = np.array([4/3,0,0])
y1 = np.array([0,4,0])
z1 = np.array([0,0,-2])
bx.plot_trisurf(x1,y1,z1, color='gold', alpha=0.6)
bx.scatter(x1,y1,z1, color='red')
bx.set_xlabel('Nilai X')
bx.set_ylabel('Nilai Y')
bx.set_zlabel('Nilai Z')
bx.set_title('3x + y - 2z = 4')


cx = fig.add_subplot(133, projection='3d')
x2 = np.array([10/7,0,0])
y2 = np.array([0,-5/3,0])
z2 = np.array([0,0,-10])
cx.set_xlabel('Nilai X')
cx.set_ylabel('Nilai Y')
cx.set_zlabel('Nilai Z')
cx.plot_trisurf(x2,y2,z2, color='blue', alpha=0.4)
cx.scatter(x2,y2,z2, color='green')
cx.set_title('7x - 6y - z = 10')
plt.show()
plt.clf()