from heapq import heappush, heappop, heapify
from collections import defaultdict
import binascii
import ITlib
import numpy

def encode(countsChar):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in countsChar.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    huf = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    hufDict = {}
    for p in huf:
        hufDict[p[0]] = p[1]
    return hufDict

def getCounts(text): 
    counts = defaultdict(int)
    for ch in text:
        counts[ch] += 1
    return counts

def string2huff(text):
    counts = getCounts(txt)
    huffDict = encode(counts)
    S = 0
    for p in huffDict:
        S += counts[p]
    print "Symbol\tWeight\tProb\tHuf Code"
    Probs = []
    for p in huffDict:
        Probs.append(counts[p]/float(S))
        print "%s\t%s\t%.5f\t%s" % (p, counts[p], counts[p]/float(S), huffDict[p])
    huffs = []
    for t in text:
        huffs.append(huffDict[t])
    return huffs, Probs

def string2ascii(text):
    ascii = [] 
    for t in text:   
        bint = bin(ord(t))[2:]
        bint = bint.zfill(7)            
        ascii.append(bint)
    return ascii


#txt = "Aw man I shot Marvin in the face".lower()
txt = "aaaaaaaaa b"
#txt = [1,2,2,2,2,2,2,3]



asciiList = string2ascii(txt)
print asciiList
huffManList, Probs = string2huff(txt)
print huffManList

nAscii = 0
for a in asciiList:
    nAscii += len(a)
nHuff = 0
for h in huffManList:
    nHuff += (len(h) + 1)

print nAscii, nHuff, float(nAscii) / nHuff
print Probs
H = ITlib.computeEntropy(numpy.array(Probs))
Hmax = ITlib.computeMaxEntropy(len(Probs))
print 1 - H/Hmax
