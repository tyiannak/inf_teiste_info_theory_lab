import ITlib, numpy
import matplotlib.pyplot as plt
import numpy

P = numpy.array( [ [0,1,1], [1,0,1], [1,1,0]])
I = numpy.eye(P.shape[0])
G = numpy.concatenate( [I, P] , axis = 1)
k, n = G.shape


print P.T
H =  numpy.concatenate([P.T, numpy.eye(n-k)], axis = 1)
print "n = %d, k = %d" % (n,k)
print "G:"
print G
print "H:"
print H

v = numpy.array([1,0,0]) 
print "Original word to be transmited: ",
print v
c = numpy.dot(v, G) % 2
print "Coded word to be transmited: ",
print c
e = numpy.zeros(c.shape)
e[3] = 1
c = (c + e) % 2
print "Coded word received (with error): ",
print c

dc = numpy.dot(c, H.T) % 2
print "Syndrome:",
print dc
if sum(dc) != 0:
    iF = (H.T.tolist()).index(dc.tolist())
    c[iF] = (c[iF] + 1) % 2
    print "Error in bit %d" % iF
    print "Corrected codeword :" ,
    print c
c = numpy.matrix(c)
#print numpy.linalg.lstsq(G.T, c.T)
#print numpy.linalg.inv(G) 