import ITlib
import string
import sys
import numpy

def huffmanCodeFromFile(filePath):
    print "Example 10: generate huffman code from a text stored in a file"
    f = open(filePath)
    text = f.read().lower()
    f.close()    
    text = ITlib.removeUnknownCharacters(text)      # remove "unknown characters"
    counts = ITlib.getTextCounts(text)              # generate histogram of characters (counts)
    huffCode, L = ITlib.generateHuffmanCode(counts) # generate huffman code
    print counts
    print huffCode
    ITlib.printTextCounts(counts, huffCode)         # print counts and huffman code 
    print "Average word length: %.2f bits" % (L)    
    P = numpy.array(counts.values()).astype(float)  # word counts to probabilities
    P /= P.sum()
    print "Entropy: %.2f bits per sample" % (ITlib.computeEntropy(P))   # compute entropy of source
    return huffCode
if __name__ == '__main__':
    huffmanCodeFromFile(sys.argv[1])
