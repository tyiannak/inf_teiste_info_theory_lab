import ITlib, numpy, itertools

P = numpy.array( [ [0,1,1], [1,0,1], [1,1,0]])

G, H = ITlib.linearCoding_computeGH(P)                  # get generator matrix and parity check matrix
k, n = G.shape
print "n = %d, k = %d" % (n,k)
print "G:"; print G
print "H:"; print H

v = numpy.array([1,0,0])                                # initial word transmited
print "Original word to be transmited:   ",
print v

c = ITlib.linearCoding_encode(G, v)                     # encoded word
print "Coded word to be transmited:      ",
print c

e = numpy.zeros(c.shape)                                # add error on 4th bit
e[3] = 1
c = (c + e) % 2
print "Coded word received (with error): ",
print c

c_corrected = ITlib.linearCoding_syndromeCorrect(H, c)  # correct with syndrome
print "Corrected code-word: ",
print c_corrected

v2 = ITlib.linearCoding_decode(G, c_corrected)          # decode
print "Decoded word", 
print v2
