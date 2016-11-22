import ITlib
import string
import sys
import numpy
import matplotlib.pyplot as plt
from scipy import signal

x = [0.1, 0.15, 0.28, 0.45, 0.75, 0.82, 0.88, 0.81, 0.55, 0.3, 0.14, -0.2, -0.5, -0.9, -0.8, -0.76, -0.75, -0.72, -0.5, -0.4, -0.33, -0.1, 0.1, 0.12, 0.22, 0.34, 0.35, 0.37]
x = numpy.array(x)
x = signal.resample(x, 102)
t = numpy.arange(0,x.shape[0])

step = 5;
x2 = x[0:x.shape[0]+step+step*2:step]
t2 = t[0:x.shape[0]+step+step*2:step]
plt.plot(t, x)
plt.stem(t2, x2, 'r')
plt.axis('off')

plt.show()