# Information Theory Library
# Author: Theodoros Giannakopoylos
from heapq import heappush, heappop, heapify
from collections import defaultdict
import binascii
import numpy
eps = 0.000000000001

def computeEntropy(Probs):
    '''
    Computes the entropy given the symbol probabilities
    ARGUMENTS:
        - Probs:        a numpy array of n probabilities (must sum to unity)
    RETURNS:
        - The computed entropy
    '''
    if numpy.abs(Probs.sum()-1.0)<eps:                              # if sum of probabilities is almost equal to 1
        ProbsNonZero = Probs[Probs>eps]                             # remove zero probabilities
        return -numpy.sum(ProbsNonZero * numpy.log2(ProbsNonZero))  # compute entropy
    else:
        raise ValueError("Probabilities must sum to unity!")        # raise an error if probabilities do not sum to 1

def computeMaxEntropy(n):
    # Returns the maximum entropy given the number of symbols
    return numpy.math.log(n, 2)

def computePriorsFromJointP(jointP):
    '''
    Computes the prior probabilities of two random variables given their joint probability matrix
    ARGUMENTS:
        - jointP:       a mxn matrix where the joint probability matrix is stored ( jointP[i,j]= P(x=i, y=j) )
    RETURNS:
        - prior probabilityes
    '''
    if numpy.abs(jointP.sum()-1.0) < eps:
        Px = jointP.sum(axis = 1)
        Py = jointP.sum(axis = 0)
        return Px, Py
    else:
        raise ValueError("Probabilities must sum to unity!")        # raise an error if probabilities do not sum to 1

def computeChannelCapacityAWGN(Badwidth, SNR):
    return Badwidth * numpy.log2(1+SNR)

def SNR_db_to_num(SNR_db):                                          # convert db to number
    return 10 ** (SNR_db / 10.0)

def SNR_num_to_db(SNR_num):                                         # convert number to db
    return 10 * numpy.log10(SNR_num)

'''''''''''''''
    CODING
''''''''''''''' 
def generateHuffmanCode(countsChar):
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
    P = numpy.array(countsChar.values()).astype(float)
    P /= P.sum()
    l = numpy.array([len(code) for code in hufDict.values()])
    averageLength = (P * l).sum()
    return hufDict, averageLength
    