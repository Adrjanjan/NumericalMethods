from math import sqrt, pi, sin
from numpy import array, transpose, roots, linspace, arange
from numpy.linalg import inv, det
import matplotlib.pyplot as plt

# 1
k = 1240 * sqrt(7)
m = 4467
l = 2j
d = k + m
c = d + l

print("k =", k)
print("m =", m)
print("l =", l)
print("d =", d)
print("c =", c)

# 2
print("{0:0.3f}".format(d))
print(d)
print("{0:0.20f}".format(d))

# 3
r = 17
h = 33
S = 2 *pi * r * (h + r)

# 5
x1 = 1
r = 2
t = 3

B = (x1 + r) / (r * sin(2 * x1) + 3.3456) * x1 ** (t * r)
print(B)

# 6
a = sqrt(2)

M = array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
M1 = inv(M)
MT = transpose(M)
detM = det(M)
print("{0}\n".format(M))
print("{0}\n".format(M1))
print("{0}\n".format(MT))
print("{0}\n".format(detM))

# 7
print("{0}\n".format(M[0][0]))
print("{0}\n".format(M[2][2]))
print("{0}\n".format(M[2][1]))

w1 = M[:, 2]
w2 = M[2, :]

# 8   -- DODAJ EWALUACJĘ WYNIKU
p = [1, -7, 3, 43, -28, -60]

print("{0}\n".format(roots(p)))

def y(x):
    return x*( x*( x*( x*( x - 7 )+ 3 ) + 43 ) - 28 ) - 60



print("{0}\n".format([y(i) for i in roots(p)]))

# 9

x = arange(-5, 5, (1.0 / 3))
print("{0}\n".format(x))

z = linspace(-5, 5, num=10)
print("{0}\n".format(z))

# 10
z = lambda x: x ** 3 - 3 * x

x = [linspace(-1, 1), linspace(-5, 5), linspace(0, 5)]

y = [[z(i) for i in x[0]], [z(i) for i in x[1]], [z(i) for i in x[2]]]

for i in range(0, 3):
    plt.plot(x[i], y[i])
    plt.title('Wykres {0}:'.format(i+1))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend('Wykres {0}'.format(i+1))
    plt.show()

# 11
m = 2.500
v = 60
multiplier_J_to_Kcal = 0.0002388458966275

def Q(m, v):
    return m * v * v / 2


print(Q(m, v)," J\n", Q(m, v) * multiplier_J_to_Kcal, " Kcal")

mass = 3
vel = linspace(200, 0)

plt.plot(vel, Q(mass, vel))
plt.title('Wykres Q(v) [skala liniowa]:')
plt.xlabel('v')
plt.ylabel('Q')
plt.legend('Ciepło w J')
plt.show()


plt.semilogy(vel, Q(mass, vel), basey=10)
plt.title('Wykres Q(v) [skala logarytmiczna]:')
plt.xlabel('v')
plt.ylabel('Q')
plt.legend('Ciepło w J')
plt.show()
