import ITlib
import string
import sys
import numpy
import matplotlib.pyplot as plt

Fa = 1000
freq = 4
ta = numpy.arange(0, 1.0+1./Fa, 1./Fa)
xa = numpy.sin(2*numpy.pi*ta*freq)
Fs1 = 50
t1 = numpy.arange(0, 1.0+1./Fs1, 1./Fs1)
x1 = numpy.sin(2*numpy.pi*t1*freq)
Fs2 = 15
t2 = numpy.arange(0, 1.0+1./Fs2, 1./Fs2)
x2 = numpy.sin(2*numpy.pi*t2*freq)
Fs3 = 5
t3 = numpy.arange(0, 1.0+1./Fs3, 1./Fs3)
x3 = numpy.sin(2*numpy.pi*t3*freq)

plt.subplot(4,1,1)
plt.plot(ta, xa)
plt.title('Analog Signal (freq = %d Hz)'%freq)
plt.axis('off')
plt.subplot(4,1,2)
plt.stem(t1, x1)
plt.title('Digital Signal (sampled at %dHz)'%Fs1)
plt.axis('off')
plt.subplot(4,1,3)
plt.stem(t2, x2)
plt.title('Digital Signal (sampled at %dHz)'%Fs2)
plt.axis('off')
plt.subplot(4,1,4)
plt.stem(t3, x3)
plt.title('Digital Signal (sampled at %dHz)'%Fs3)
plt.axis('off')

plt.show()