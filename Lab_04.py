import matplotlib.pyplot as plt
from numpy import linspace, polyfit, poly1d, array
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
start = -2
end = 2
n = 21

w_rownoodlegle = linspace(start, end, 21)
w_czebyszewa   = array([(start+end)/2 + (end - start)/2 *cos(pi*(2*k+1)/(2*n)) for k in range(1, n)])
f = lambda x: 1/(25*x**2 +1)


wielom_rowno = poly1d(polyfit(w_rownoodlegle, f(w_rownoodlegle), deg=n-1))
wielom_czeb  = poly1d(polyfit(w_czebyszewa, f(w_czebyszewa), deg=n-1))

sklej_rowno = interp1d(w_rownoodlegle, f(w_rownoodlegle), kind=3)
sklej_czeb  = interp1d(w_czebyszewa, f(w_czebyszewa), kind=3)

plt.plot(w_rownoodlegle, wielom_rowno(w_rownoodlegle), label='Węzły Rownoodległe')
plt.plot(w_czebyszewa, wielom_czeb(w_czebyszewa), label='Węzły Czebyczewa')
plt.scatter(w_rownoodlegle, wielom_rowno(w_rownoodlegle))
plt.scatter(w_czebyszewa, wielom_czeb(w_czebyszewa))
plt.title('Wykres wykonany przy pomocy interpolacji wielomianowej:')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

plt.plot(w_rownoodlegle, sklej_rowno(w_rownoodlegle), label='Węzły Rownoodległe')
plt.plot(w_czebyszewa, sklej_czeb(w_czebyszewa), label='Węzły Czebyczewa')
plt.scatter(w_rownoodlegle, sklej_rowno(w_rownoodlegle))
plt.scatter(w_czebyszewa, sklej_czeb(w_czebyszewa))
plt.title('Wykres wykonany przy pomocy interpolacji funkcjiami sklejanymi:')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

3 #

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
