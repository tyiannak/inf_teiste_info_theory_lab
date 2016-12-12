import ITlib
import random
print "Example 13: Compare Shannon-Fano and Huffman Codes Example"

charCounts = {'a':7, 'b':6, 'c':9, 'd':19, 'e':7}
hcode, l1 = ITlib.generateHuffmanCode(charCounts)
sfcode, l2 = ITlib.generateShannonFanoCode(charCounts) 

print "\nShannon Fano Code:"
print sfcode
print "Length %.2f" % (l2)
print "\nHuffman  Code:"
print hcode
print "Length %.2f" % (l1)


'''
# TEMP: this is used to generate examples where huffman is bettern than sf
maxVal = 20
nExp = 100000
for i in range(nExp):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    d = random.randint(1, maxVal)
    e = random.randint(1, maxVal)

    charCounts = {'a':a, 'b':b, 'c':c, 'd':d, 'e':e}                    
    code, l1 = ITlib.generateHuffmanCode(charCounts)
    code, l2 = ITlib.generateShannonFanoCode(charCounts) 
    #print charCounts, l1, l2
    if l1+0.05<l2:
        print charCounts, l2-l1
'''