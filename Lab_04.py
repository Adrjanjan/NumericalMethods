
import matplotlib.pyplot as plt
import time
from numpy import linspace, polyfit, poly1d, array
from math import pi, cos
from scipy.interpolate import interp1d

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

start = -2
end = 2
n = 21

w_rownoodlegle = linspace(start, end, 21)
w_czebyszewa   = array([(start+end)/2 + (end - start)/2 *cos(pi*(2*k+1)/(2*n)) for k in range(1, n)])
f = lambda x: 1/(25*x**2 +1)


wielom_rowno = poly1d(polyfit(w_rownoodlegle, f(w_rownoodlegle), deg=15))
wielom_czeb  = poly1d(polyfit(w_czebyszewa, f(w_czebyszewa), deg=15))

sklej_rowno = interp1d(w_rownoodlegle, f(w_rownoodlegle), kind=3)
sklej_czeb  = interp1d(w_czebyszewa, f(w_czebyszewa), kind=3)

plt.plot(w_rownoodlegle, wielom_rowno(w_rownoodlegle), label='Węzły Rownoodległe')
plt.plot(w_czebyszewa, wielom_rowno(w_czebyszewa), label='Węzły Czebyczewa')
plt.scatter(w_rownoodlegle, wielom_rowno(w_rownoodlegle))
plt.scatter(w_czebyszewa, wielom_rowno(w_czebyszewa))
plt.title('Wykres wykonany przy pomocy interpolacji wielomianowej:')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

plt.plot(w_rownoodlegle, sklej_rowno(w_rownoodlegle), label='Węzły Rownoodległe')
plt.plot(w_czebyszewa, sklej_rowno(w_czebyszewa), label='Węzły Czebyczewa')
plt.scatter(w_rownoodlegle, sklej_rowno(w_rownoodlegle))
plt.scatter(w_czebyszewa, sklej_rowno(w_czebyszewa))
plt.title('Wykres wykonany przy pomocy interpolacji funkcjiami sklejanymi:')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
