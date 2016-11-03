import ITlib
from nltk.corpus import stopwords
import numpy
import re

stopwords = ["i'm","don't","it's","i'll","you're","the","of","and","to","a","in","for","is","on","that","by","this","with","i","you","it","not","or","be","are","from","at","as","your","all","have","new","more","an","was","we","will","home","can","us","about","if","page","my","has","search","free","but","our","one","other","do","no","information","time","they","site","he","up","may","what","which","their","news","out","use","any","there","see","only","so","his","when","contact","here","business","who","web","also","now","help","get","pm","view","online","c","e","first","am","been","would","how","were","me","s","services","some","these","click","its","like","service","x","than"]

def readTxtAndComputeEntropy(fileName):
    print "filename: " + fileName
    f = open(fileName, "r")
    text = f.read()
    f.close()    
    words = re.findall(r"[\w']+", text)    
    words2 = [w.lower() for w in words]
    words3 = [word for word in words2 if word not in stopwords]
    terms = []
    weights = []
    for w in words3:
        if w.lower() in terms:
            weights[terms.index(w.lower())] += 1
        else:
            terms.append(w.lower())
            weights.append(1)    
    terms2 = [t for (w, t) in sorted(zip(weights, terms), reverse = True)]
    weights2 = numpy.array(sorted(weights, reverse = True)).astype(float)
    weights  = numpy.array(sorted(weights, reverse = True))
    weights2 = weights2 / weights2.sum()    
    H = ITlib.computeEntropy(weights2)
    Hmax = ITlib.computeMaxEntropy(float(len(terms2)))
    P = 1 - H/Hmax
    print "H=%.2f\tHmax=%.2f\tRed.=%.1f%%" % (H, Hmax, 100*P)

print "\nExample 5"
print "Parse the lyrics from 5 songs and compute the entropies (after removing stopwords)\n"

readTxtAndComputeEntropy("data/lyrics/pinkfloyd_time"); print
readTxtAndComputeEntropy("data/lyrics/eminem_rapgod"); print
readTxtAndComputeEntropy("data/lyrics/ladygaga_badromance"); print
readTxtAndComputeEntropy("data/lyrics/beatles_lovemedo"); print
readTxtAndComputeEntropy("data/lyrics/mosdef_mathematic"); print
