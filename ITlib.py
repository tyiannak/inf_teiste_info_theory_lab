# Information Theory Library
# Author: Theodoros Giannakopoylos
from heapq import heappush, heappop, heapify
from collections import defaultdict
import binascii
import numpy
import string
import operator
eps = 0.000000000001

#listOfAllCharacters = string.printable[:-3]
#listOfAllCharacters = string.ascii_lowercase + ",.?!-() \t\n\"#$%%+*/^"
listOfAllCharacters = "0123456789abcdefghijklmnopqrstuvwxyz!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n"

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
    # Generate the Huffman code for the given dict mapping symbols to weights
    # INPUT: countsChar: a dictionary of chars to counts
    # RETURNS: huffman code and average code word length    

    for c in countsChar:
        if countsChar[c] == 0:
            countsChar[c] = 1
    heap = [[wt, [sym, ""]] for sym, wt in countsChar.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]+0.0000000001] + lo[1:] + hi[1:])
    huf = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    hufDict = {}
    for p in huf:
        hufDict[p[0]] = p[1]
    P = numpy.array(countsChar.values()).astype(float)
    P /= P.sum()
    l = numpy.array([len(code) for code in hufDict.values()])
    averageLength = (P * l).sum()
    return hufDict, averageLength
    
def getTextCounts(text): 
    # Get counts of each character of a given string (message)    
    # INPUT: text (string)
    # RETURNS: a dictionary of chars->counts
    counts = dict.fromkeys(listOfAllCharacters, 0)
    for ch in text:
        if ch in counts:
            counts[ch] += 1
    return counts

def printTextCounts(counts, code = None):
    # Prints in sorted order the provided character counts and code words (if provided)
    # ARGUMENTS:
    #  - counts: dictionary of chars->counts
    #  - code: dictionary of chars->code words    
    Sum = float(sum(counts.values()))
    sorted_counts = sorted(counts.items(), key=operator.itemgetter(1), reverse = True)
    print sorted_counts
    for key, count in sorted_counts:                
        k = key
        if key == "\t":
            k = "\\t"
        if key == "\n":
            k = "\\n"        
        if key == " ":
            k = "space"    
        if not code:
            print "%s\t%.2f%%" % (k, 100 * counts[key] / Sum)
        else:
            print "%s\t%.2f%%\t%s" % (k, 100 * counts[key] / Sum, code[key])

def removeUnknownCharacters(str):
    # removes special characters from string and returns new string
    strNew = []
    for s in str:
        if s in listOfAllCharacters:
            strNew.append(s)
    return ''.join(strNew)

def encode(code, text):    
    # Encodes a text using a given code (extracted e.g. from generateHuffmanCode() function)    
    # ARGUMENTS:
    #  - code: dictionary of chars->code words    
    #  - text: string to be encoded
    # RETURNS:
    #  - eW: list of encoded words
    eW = []
    for t in text:
        eW.append(code[t])
    return eW

def generateShannonFanoCode(countsChar):
    # Generate the Shanno-Fano code for the given dict mapping symbols to weights
    # INPUT: countsChar: a dictionary of chars to counts
    # RETURNS: ShannoFeno code and average code word length    

    for c in countsChar:
        if countsChar[c] == 0:
            countsChar[c] = 1
    sDict = shannonFanoTree2Dictionary(calucateShannonFanoTree(countsChar))
    P = numpy.array(countsChar.values()).astype(float)
    P /= P.sum()
    l = numpy.array([len(code) for code in sDict.values()])
    averageLength = (P * l).sum()
    return sDict, averageLength

def divideShannonFanoList(counts): 
    '''
    Divides a list of (symbol, frequency) pairs according to the Shannon-Fano algorithm
    '''
    counts2 = counts.items()
    counts2 = sorted(counts2, key=lambda x: x[1], reverse = True)    
    Sum = sum([c[1] for c in counts2])
    S = []        
    for i, p in enumerate(counts2):
        S.append(abs(sum([c[1] for c in counts2[0:i]]) - sum([c[1] for c in counts2[i::]])))
    imin = numpy.argmin(S)    
    left = [l[0] for l in counts2[0:imin]]
    right = [l[0] for l in counts2[imin::]]       
    return left, right

def shannonFanoTree2Dictionary(tree):
    '''
    Shannon-Fano coding: Transcode tree to python 
    '''    
    code_words = dict()
    level = 1    
    if len(tree) == 2 and isinstance(tree,tuple):
        l, r = tree
        cl, cr = shannonFanoTree2Dictionary(l), shannonFanoTree2Dictionary(r)        
        sfCode = dict()
        for k,v in cl.iteritems():
            sfCode[k] = '0'+v
        for k,v in cr.iteritems():
            sfCode[k] = '1'+v
        return sfCode
    else:
        return {tree:''}

def calucateShannonFanoTree(dc):
    '''
    Calculates the tree that represents the shannon fano coding, given a dictionary of symbol probabilities
    '''
    tree = (None,None)
    if len(dc) == 1:
        return dc.keys()[0]
    else:
        left, right = divideShannonFanoList(dc)                
        dl = {}; dr = {}
        for x in left:
            dl[x] = dc[x]
        for x in right:
            dr[x] = dc[x]
        tree = (calucateShannonFanoTree(dl), calucateShannonFanoTree(dr))
        return tree
