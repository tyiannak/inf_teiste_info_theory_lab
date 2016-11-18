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
    code1 = huffmanCodeFromFile('data/americanCivilWarWiki.txt')
    code2 = huffmanCodeFromFile('data/pythonCode.txt')
    code3 = huffmanCodeFromFile('data/annotationCSV.txt')
    text1 = "Aw, man, I shot Marvin in the face.".lower()
    t11 = ITlib.encodeHuffman(code1, text1)
    t12 = ITlib.encodeHuffman(code2, text1)
    t13 = ITlib.encodeHuffman(code3, text1)
    L11 = 0
    print "Testing text %s (%d characters)"%(text1, len(text1))
    for t in t11:
        print t,
        L11 += len(t)
    print "Length: %d"%L11
    L12 = 0
    for t in t12:
        print t,
        L12 += len(t)
    print "Length: %d"%L12
    L13 = 0
    for t in t13:
        print t,
        L13 += len(t)
    print "Length: %d"%L13
    print 
    text2 = " for pair in lo[1:]:  pair[1] = '0'".lower()
    t21 = ITlib.encodeHuffman(code1, text2)
    t22 = ITlib.encodeHuffman(code2, text2)
    t23 = ITlib.encodeHuffman(code3, text2)
    L21 = 0
    print "Testing text %s (%d characters)"%(text2, len(text2))
    for t in t21:
        print t,
        L21 += len(t)
    print "Length: %d"%L21
    L22 = 0
    for t in t22:
        print t,
        L22 += len(t)
    print "Length: %d"%L22
    L23 = 0
    for t in t23:
        print t,
        L23 += len(t)
    print "Length: %d"%L23
