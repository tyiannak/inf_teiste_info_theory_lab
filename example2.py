import ITlib
import numpy
import matplotlib.pyplot as plt

print "\nExample 2"
print "Entropy example for a binary source\n"

step = 0.001
p1 = numpy.arange(0,1+step,step)                            # p1 defined in the [0,1] range
p2 = 1 - p1                                                 # p2 = 1 - p1
H = numpy.zeros(p1.shape)                                   # entropy initialization
for i in range(p1.shape[0]):                                # for each p value
    Probs = numpy.array([p1[i], p2[i]])                     # define probabiitlies matrix
    H[i] = ITlib.computeEntropy(Probs)                      # compute entropy
plt.plot(p1, H)
plt.xlabel("p1")
plt.ylabel("Entropy")
plt.show()
