import numpy as np
# from sympy.matrices import Matrix
# from sympy.abc import x, y, z, g, W, V, U, B, p
from sympy import *
x, y, z, g, w, v, u, b, p, c = symbols('x y z g W V U B p c', constant = True)
import cmath
from sympy import pprint, matrix_multiply_elementwise

A = Matrix([[x + x*1j, y],[x, z]])
B = Matrix([[x - z*1j, x],[y - y*2j, y]])

r1 = Matrix([[-1j*g*u - 1j*p*b, -1j*g/np.sqrt(2)*w - g/np.sqrt(2)*v, 0]])
r2 = Matrix([[-1j*g/np.sqrt(2)*w + g/np.sqrt(2)*v, -1j*p*b, -1j*g/np.sqrt(2)*w - g/np.sqrt(2)*v]])
r3 = Matrix([[0, -1j*g/np.sqrt(2)*w + g/np.sqrt(2)*v, -1j*g*u + 1j*p*b]])
phi = Matrix([[0],[0], [c/np.sqrt(2)]])


D = Matrix([[r1], [r2], [r3]])
D_dag = D.H
phi_dag = phi.H

kin = phi_dag*D_dag*D*phi

C = A*B
# print(C)
print(kin)

