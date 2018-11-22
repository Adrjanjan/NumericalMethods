import matplotlib.pyplot as plt
from numpy import linspace, polyfit, poly1d, array, arange
from math import pi, cos
from scipy.interpolate import interp1d
# 1 #
def lagrange_interpolation(x, y):
    assert len(x) == len(y) != 0
    def f(n):
        sum = 0
        for i in range(len(x)):
            prod = 1
            for j in range(len(x)):
                if(i != j):
                    prod *= (n - x[j])/(x[i] - x[j])
            sum += y[i] * prod
        return sum
    return f
z= [-2, -1, 0, 1, 2]
y = lagrange_interpolation(z, [(2*(x*x)-2) for x in z])

# plt.plot(linspace(-10, 10), y(linspace(-10, 10)))
# plt.title('Wykres:')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# 2 #
f = lambda x: 1/(25*x**2 +1)
start = -2
end = 2
n = 21
x = arange(-2,2,0.05)

rownoodlegle_X = linspace(start, end, n)
czebyszew_X   = array([(start + end) / 2 + (end - start) / 2 * cos(pi * (2 * k + 1) / (2 * n)) for k in range(1, n)])

wielomian_rownoodlegle = poly1d(polyfit(rownoodlegle_X, f(rownoodlegle_X), deg=(n - 1)))
wielomian_czebyszew  = poly1d(polyfit(czebyszew_X, f(czebyszew_X), deg=(n - 1)))

rownoodlegle_Y_wiel = wielomian_rownoodlegle(x)
czebyszew_Y_wiel = wielomian_czebyszew(x)

spline_rownoodlegle = interp1d(rownoodlegle_X, f(rownoodlegle_X), 3, fill_value='extrapolate')
spline_czebyszew  = interp1d(czebyszew_X, f(czebyszew_X), 3, fill_value='extrapolate')

rownoodlegle_Y_spline = spline_rownoodlegle(x)
czebyszew_Y_spline = spline_czebyszew(x)


plt.plot(x, rownoodlegle_Y_wiel, label='Węzły Rownoodległe')
plt.plot(x, czebyszew_Y_wiel, label='Węzły Czebyczewa')
plt.scatter(rownoodlegle_X, wielomian_rownoodlegle(rownoodlegle_X))
plt.scatter(czebyszew_X, wielomian_czebyszew(czebyszew_X))
plt.title('Wykres wykonany przy pomocy interpolacji wielomianowej:')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.ylim(-0.5,1.5)
plt.figure(figsize=(15,10))
plt.show()

plt.plot(x, rownoodlegle_Y_spline, label='Węzły Rownoodległe')
plt.plot(x, czebyszew_Y_spline, label='Węzły Czebyczewa')
plt.scatter(rownoodlegle_X, wielomian_rownoodlegle(rownoodlegle_X))
plt.scatter(czebyszew_X, wielomian_czebyszew(czebyszew_X))
plt.title('Wykres wykonany przy pomocy interpolacji funkcjiami sklejanymi:')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# 3 #

napiecie = [x for x in range(-10, 11)]
predkosc = [-9.1, -8.82, -7.99, -7.1, -6.32, -5.33, -4.73, -3.65, -2.53, -1.28, 0.0, 1.26, 2.49, 3.61, 4.61, 5.51, 6.32, 7.1, 7.81, 8.45, 9.02]

V = lagrange_interpolation(napiecie, predkosc) # <- wielomian Lagrange'a




# 4 #

czas = [x for x in range(0, 4)]
polozenie = [0.0, 42.7, 73.2, 92.5]

V2 = lagrange_interpolation(polozenie, czas)

czas2 = V2(79.6)

predkosc = 79.6/czas2

print("V(t) = {0} m/s\n czas minięcia = {1} s".format(predkosc, czas2))
