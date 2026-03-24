import numpy as np # allows the use of arrays, and provides many useful functions
import matplotlib.pyplot as plt # plotting functionality
from scipy import integrate # numerical integration tool for ode's

x = np.array([[0,0,0,1],
              [1,1,1,1],
              [0,0,1,0],
              [3,2,1,0]])
print(x)

M = np.linalg.inv(x)

P1 = np.array([0,0,0])
P2 = np.array([3,0,0])

R1 = np.array([1,0,0])
R2 = np.array([3,0,0])

G = np.vstack((P1,P2,R1,R2))

print(M@G)