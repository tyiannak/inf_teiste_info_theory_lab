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
def huffman(p):
    # Generates a huffman code (i.e. mappings of characters to binary words), given a list of probs (one for each character)
    # Arguments:
    #  - countsChair:   a dict of characters-frequqncies
    # Returns:
    #  - huffDict:      a dict of characters-binary huffman words    

    print sum(p.values())
    #assert(sum(p.values()) == 1.0)          # Ensure probabilities sum to 1

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(p) == 2):
        return dict(zip(p.keys(), ['0', '1']))

    # Create a new distribution by merging lowest prob. pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c

def lowest_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities.'''
    assert(len(p) >= 2) # Ensure there are at least 2 symbols in the dist.

    sorted_p = sorted(p.items(), key=lambda (i,pi): pi)
    return sorted_p[0][0], sorted_p[1][0]

INF = 1e999

def min_argmin(array):
    """Returns the minimum element of an array, and its index."""
    mn = min(array)
    return (mn, array.index(mn))

def huffman2(probs):
    """Return Huffman codewords for the given probability distribution."""
    nodes = [[x] for x in range(len(probs))]
    merged_probs = probs[:]
    while len(nodes) > 1:
        # find two least probable nodes:
        (mn, idx) = min_argmin(merged_probs)
        merged_probs[idx] = INF
        (mn2, idx2) = min_argmin(merged_probs)
        # merge them:
        merged_probs[idx] = mn + mn2;
        del merged_probs[idx2]
        nodes[idx] = [nodes[idx], nodes[idx2]]
        del nodes[idx2]

    # Recursive navigation of tree of nested lists to construct codes
    def huffman_helper(cur_code, nodes, codes):
        if len(nodes) == 1:
            symbol = nodes[0]
            codes[symbol] = cur_code
        else:
            huffman_helper(cur_code + '0', nodes[0], codes)
            huffman_helper(cur_code + '1', nodes[1], codes)
    codes = ['' for x in range(len(probs))]
    huffman_helper('', nodes[0], codes)
    return codes    

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
    