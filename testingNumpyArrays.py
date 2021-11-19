import numpy as np

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
    trans = transMatrices[0]
    for i in range(len(transMatrices)-1):
        trans = np.dot(trans,transMatrices[i+1])
    return(trans)

def c(angle):
    return(np.cos(np.deg2rad(angle)))

def s(angle):
    return(np.sin(np.deg2rad(angle)))

def check(a,b):
    print()
    print()
    print()
    if np.allclose(a,b,atol=0.002):
        print("Match")
    else:
        print("No Match")

phi = 90 #in k
beta = 20 #in j
gamma = -30 #in j

T_1I = Tz(phi)
T_21 = Ty(beta)
T_32 = Ty(gamma)

T_2I = combineTrans([T_21,T_1I])
T_2I = T_2I.round(3)
print(T_2I)

T_3I = combineTrans([T_32,T_21,T_1I])
T_3I = T_3I.round(3)

actual_T_2I = np.array([[c(beta)*c(phi),c(beta)*s(phi),-s(beta)],
                        [-s(phi),c(phi),0],
                        [s(beta)*c(phi),s(beta)*s(phi),c(beta)]])

y = gamma
b = beta
p = phi
actual_T_3I = np.array([[c(gamma)*c(beta)*c(phi)-s(gamma)*s(beta)*c(phi),c(gamma)*c(beta)*s(phi)-s(gamma)*s(beta)*s(phi),-c(gamma)*s(beta)-s(gamma)*c(beta)],
                        [-s(p),c(p),0],
                        [s(y)*c(b)*c(p)+c(y)*s(b)*c(p),s(y)*c(b)*s(p)+c(y)*s(b)*s(p),-s(y)*s(b)+c(y)*c(b)]])

print(actual_T_2I.round(3))

check(T_2I,actual_T_2I)
print("Layer 3")
check(T_3I,actual_T_3I)

#print(actual_T_3I.round(3))
#print()
#print(T_3I)






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
'''
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

fig = plt.figure()
# syntax for 3-D projection
ax = plt.axes(projection='3d')

# defining all 3 axes
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)

ax.plot3D(x, y, z, 'green')
ax.set_title('3D line plot geeks for geeks')
plt.show()'''


