import ITlib

print "Example 12: generate shannon-fano code from a list of character counts (same as example9.py for Huffman)"

charCounts = {'a':5, 'b':15, 'c':1, 'd':20, 'e':25}
code, length = ITlib.generateShannonFanoCode(charCounts)
print code, length

charCounts = {'a':10, 'b':6, 'c':2}
code, length     = ITlib.generateShannonFanoCode(charCounts)
print code, length

charCounts = {'a':1, 'b':50, 'c':10,'d':5}
code, length = ITlib.generateShannonFanoCode(charCounts)
print code, length

charCounts = {'a':5, 'b':4, 'c':15,'d':5,'e':6}
code, length = ITlib.generateShannonFanoCode(charCounts)
print code, length
