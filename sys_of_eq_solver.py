import numpy as np

A = np.array([[1, 2, 3]])
B = np.array([[2, 4, 6]])

BT = np.transpose(B)
BTT = B.T

print(BT)
print(BTT)

print(A)
C = np.dot(A, BT)
print(C)

D = np.array([[1,1,1]])
DT = D.T
E = np.dot(D, DT)

t = int( E + 7 )

print(t)