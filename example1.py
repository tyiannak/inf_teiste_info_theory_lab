import ITlib, numpy
import matplotlib.pyplot as plt

def computeChannelEntropies(jointProbMatrix):
    [Px, Py] = ITlib.computePriorsFromJointP(jP)
    print "P(x)", Px
    print "P(y)", Py
    Hx = ITlib.computeEntropy(Px)
    Hy = ITlib.computeEntropy(Py)
    Hjoint = ITlib.computeEntropy(jP.flatten())
    Hcond =  Hjoint - Hy
    print "H(x) = %.4f" % Hx
    print "H(y) = %.4f" % Hy
    print "H(x,y) = %.4f" % Hjoint
    print "H(x|y) = %.4f" % Hcond

print "\nExample 1"
print "Compute channel entropies given the joint probabilities between the input and the ouput of a channel\n"
jP = numpy.array([[1.0/4, 1.0/16, 0],[1.0/4, 1.0/8, 0],[0.0, 1.0/16, 1.0/4.0]])
print "Joint probability matrix is "
print jP
computeChannelEntropies(jP)

