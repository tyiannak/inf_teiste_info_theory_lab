import ITlib
import numpy
import os
import matplotlib.pyplot as plt

def generateSymbols(nSymbols):
    return [numpy.random.choice(["a","b","c"], p=[0.1,0.2,0.7]) for i in range(nSymbols)]

def computeProbsFromSymbols(symbols):
    Pa = float(symbols.count("a")) / len(symbols)
    Pb = float(symbols.count("b")) / len(symbols)
    Pc = float(symbols.count("c")) / len(symbols)
    return (Pa, Pb, Pc)

print "\nExample 2"
print "Simulation of estimating entropy of messages of different length\n"

nSymbols = range(10,20,2)+range(25,105,5)+range(200,2000,100)+range(5000,100000,5000)

Hs = []
realEntropy = ITlib.computeEntropy(numpy.array([0.1,0.2,0.7]))
for nS in nSymbols:
    print "Estimating entropy for %d symbols per message " % nS, 
    symbols = generateSymbols(nS)
    (Pa, Pb, Pc) = computeProbsFromSymbols(symbols)
    Hs.append(ITlib.computeEntropy(numpy.array([Pa, Pb, Pc])))
    print "P(a)=%.2f P(b)=%.2f P(c)=%.2f --> H=%.3f" % (Pa, Pb, Pc, Hs[-1])

plt.plot(numpy.log10(nSymbols), Hs); 
plt.plot(numpy.log10(numpy.array([nSymbols[0],nSymbols[-1]])), [realEntropy, realEntropy],"--")
plt.xlabel("log(nsymbols)"); plt.show()

