import ITlib

print "Example 9: generate huffman code from a list of character counts"

charCounts = {'a':5, 'b':15, 'c':1, 'd':20, 'e':25}
huffCode = ITlib.generateHuuffmanCode(charCounts)
print huffCode

charCounts = {'a':10, 'b':6, 'c':2}
huffCode = ITlib.generateHuuffmanCode(charCounts)
print huffCode

charCounts = {'a':1, 'b':50, 'c':10,'d':5}
huffCode = ITlib.generateHuuffmanCode(charCounts)
print huffCode

charCounts = {'a':5, 'b':4, 'c':15,'d':5,'e':6}
huffCode = ITlib.generateHuuffmanCode(charCounts)
print huffCode


#print ITlib.huffman2([30, 30, 13, 12, 10, 5])