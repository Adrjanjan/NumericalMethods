import matplotlib.pyplot as plt
from numpy import linspace
from math import exp, fabs
from scipy.optimize import bisect, newton
import time

def f(x):
    return exp(-2*x)+x*x-1

def f_1(x):
    return -2*exp(-2*x) + 2*x

def f_2(x):
    return 4*exp(-2*x) + 2

x = linspace(-1, 5)


def bisection(function, a, b, delta, max_iter):
    if (function(a) * function(b)> 0) or (max_iter <= 0):
        return [float('nan'), -1]

    count = 0
    prev_val = function(b)
    mid = a + (b - a) / 2.0

    while (count < max_iter):
        count += 1
        mid = a + (b - a) / 2.0
        val = function(mid)

        if (val == 0.0):
            return [mid, count]

        if (function(a) * function(mid) < 0):
            b = mid
        else:
            a = mid


        if(fabs(val - prev_val) < delta):
            return [mid,count]

        prev_val = val
        mid = a + (b - a) / 2.0

    return [mid, count]

def stycznych_newton(function, a, b, delta, max_iter, f_prime, f_bis):
    if (function(a) * function(b)> 0) or (max_iter <= 0):
        return [float('nan'), -1]

    if(function(a)*f_bis(a) > 0):
        cur_x = a
    elif(function(b)*f_bis(b) > 0):
        cur_x = b
    else:
        return [float('nan'), -1]

    if(function(cur_x) == 0):
        return [cur_x, 0]

    count = 0
    prev_x = cur_x

    while (count < max_iter):
        count += 1

        cur_x = prev_x - function(prev_x)/f_prime(prev_x)

        if (function(cur_x) == 0.0):
            return [cur_x, count]


        if(fabs(cur_x - prev_x) < delta):
            return [cur_x,count]

        prev_x = cur_x

    return [cur_x, count]

def siecznych(function, a, b, delta, max_iter, f_prime, f_bis):
    if (function(a) * function(b)> 0) or (max_iter <= 0):
        return [float('nan'), -1]

    if(function(a)*f_bis(a) > 0):
        prev_x_1 = a
        prev_x_2 = b
    elif(function(b)*f_bis(b) > 0):
        prev_x_1 = b
        prev_x_2 = a
    else:
        return [float('nan'), -1]

    if(function(prev_x_1) == 0):
        return [prev_x_1, 0]

    count = 0

    while (count < max_iter):
        count += 1
        cur_x = prev_x_1 - function(prev_x_1)/(function(prev_x_2) - function(prev_x_1)) * (prev_x_2 - prev_x_1)

        if (function(cur_x) == 0.0):
            return [cur_x, count]

        if(fabs(cur_x - prev_x_1) < delta):
            return [cur_x,count]

        prev_x_2 = prev_x_1
        prev_x_1 = cur_x

    return [cur_x, count]