import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import time

Transformations = []

def Tx(angle):
    angleRad = np.deg2rad(angle)
    return np.array([[1,0,0],[0,np.cos(angleRad),np.sin(angleRad)],[0,-np.sin(angleRad),np.cos(angleRad)]])

def Ty(angle):
    angleRad = np.deg2rad(angle)
    return np.array([[np.cos(angleRad),0,-np.sin(angleRad)],[0,1,0],[np.sin(angleRad),0,np.cos(angleRad)]])

def Tz(angle):
    angleRad = np.deg2rad(angle)
    return np.array([[np.cos(angleRad),np.sin(angleRad),0],[-np.sin(angleRad),np.cos(angleRad),0],[0,0,1]])

def combineTrans(transMatrices):
    trans = transMatrices[-1]
    for i in len(transMatrices):
        trans = np.dot()

phi = 90 #in k
beta = 20 #in j
gamma = -30 #in j

T_1I = Tz(phi)
T_21 = Ty(beta)
T_32 = Ty(beta)

T_3I = combineTrans([T_32,T_21,T_1I])

'''T_1I = Tx(90)
print("Transformation Matrix")
print(T_1I)
print()

T_21 = Tx(45)
print("Transformation Matrix 2")
print(T_21)

pos_vector = np.array([0,1,0])
print("pos_vector")
print(pos_vector)
print()

print("Result")
result = np.dot(T_1I,pos_vector)
result = result.round(1)
print(result)
print()

print("Result")
result = np.dot(T_21,T_21)
result = result.round(1)
print(result)
T_1I = T_1I.round(1)
print(T_1I)'''










#Plotting Stuff
'''fig = plt.figure()
# syntax for 3-D projection
ax = plt.axes(projection='3d')

# defining all 3 axes
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)

ax.plot3D(x, y, z, 'green')
ax.set_title('3D line plot geeks for geeks')
plt.show()'''


