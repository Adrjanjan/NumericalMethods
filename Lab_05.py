import numpy

import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = numpy.array([0,5,10,15,20,30,40,50])
y = numpy.array([0,0,0,12,40,40,40,40])

coeffs = numpy.polyfit(x, y, deg=4) #you can change degree as you see fit
poly = numpy.poly1d(coeffs)
yp = numpy.polyval(poly, x)

interpLength = 10
new_x = numpy.linspace(x.min(), x.max(), interpLength)
new_y = interp1d(x, y, kind='cubic')(new_x)


plt.plot(x, y, '.', x, yp, '-', new_x,new_y, '-')
plt.show()