# 1
import math
import matplotlib.pyplot as plt

p = [math.pi, math.e, 10**math.pi, math.factorial(9)]
p_ = [22/7, 2.718, 1397, (18*math.pi)**0.5*(9/math.e)**9]

# A
for i in range(p.__len__()):
    err = math.fabs(p[i] - p_[i])
    abs_err = math.fabs(err/p[i])
    print(err)
    print(abs_err)


# 2
def G(p, n=1):
    if n == 1:
        return (10**p*(1+p*round(math.pi, 15)*10**(-p))-10**p)/p
    return [G(x) for x in range(1, n+1)]


# A Nie, nie zależy, zawsze wynosi math.pi.
# B
# C Wraz ze wzrostrem n wzrasta błąd.
# D Jest to błąd zaokrągleń do 17 pozycji, później błąd reprezentacji.

n = 50

w_ = G(1, n)
err = [math.fabs(i-math.pi) for i in w_]
abs_err = [math.fabs(i/math.pi) for i in err]
print(w_)
print(err)
print(abs_err)

plt.semilogy([i for i in range(n)], abs_err, basey=10)
plt.title('Wykres  zależności wartości obliczonej od n:')
plt.xlabel('n')
plt.ylabel('G(n)')
plt.legend('G')
plt.show()


# 3
def exp2(n):
    sum = 0
    for i in range(0, n + 1):
        sum += 1/math.factorial(i)
    return sum


e1 = exp2(5)
e2 = exp2(10)

err = [math.fabs(math.e - e1), math.fabs(math.e - e2)]
abs_err = [x/math.e for x in err]
print(err)
print(abs_err)

# 4
a = 1.0
b = 0.1
for i in range(50, 55):
    b= 2**(-i)
    print(a + b- a - b)
print(2**(-52))
## ANSWER  B = 2^-52, zatem 52 bity mantysy
## Z błędem obcięcia majacym miejsce od liczb mniejszych od 2^-52


# 5
n=1000
PI = (math.fsum([1/(x*x) for x in range(1, n)])*6)**0.5
print(PI)
# mamy tu do czynienia z błędami obcięcia (skończona liczba elementów tej nieskończonej sumy),
# błędami zaokrągleń (bardzo małe liczby w kolejnych krokach sumy).