import ITlib

print "Example 9: generate huffman code from a list of character counts"

charCounts = {'a':5, 'b':15, 'c':1, 'd':20, 'e':25}
huffCode, length = ITlib.generateHuffmanCode(charCounts)
print huffCode, length

charCounts = {'a':10, 'b':6, 'c':2}
huffCode, length     = ITlib.generateHuffmanCode(charCounts)
print huffCode, length

charCounts = {'a':1, 'b':50, 'c':10,'d':5}
huffCode, length = ITlib.generateHuffmanCode(charCounts)
print huffCode, length

charCounts = {'a':5, 'b':4, 'c':15,'d':5,'e':6}
huffCode, length = ITlib.generateHuffmanCode(charCounts)
print huffCode, length
