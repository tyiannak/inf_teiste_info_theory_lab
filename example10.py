import ITlib
import string

print "Example 10: generate huffman code from a list of character counts"

#charCounts
f = open("/home/tyiannak/Desktop/usa_history1.txt", "r")
text = f.read()
f.close()    
text = text.lower()
print text

d = dict.fromkeys(string.ascii_lowercase, 0)
for t in text:    
    if t in d:        
        d[t] += 1

huffCode = ITlib.generateHuuffmanCode(d)
print huffCode

# TODO: apply code on other texts (and compare with binary)
#print ITlib.huffman2([30, 30, 13, 12, 10, 5])