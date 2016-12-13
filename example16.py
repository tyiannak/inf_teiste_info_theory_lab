import ITlib
import sys
if __name__ == '__main__':
    text = sys.argv[1]    
    LenBytes = len(text)
    LenBits = LenBytes * 8
    print "Initial text (%d bytes = %d bits): %s" % (LenBytes, LenBits, text)
    print "Code:"    
    charCounts = ITlib.getTextCountsUnique(text)    
    code, length = ITlib.generateHuffmanCode(charCounts)            # generate huffman code
    ITlib.printTextCounts(charCounts, code)                         # print word counts and statistics
    etext = ITlib.encode(code, text)                                # encode using huffman code    
    etext = "".join(etext)                                          # convert list to string
    LenBitsEncoded = len(etext)
    print "Encoded text (%d bits): %s" % (LenBitsEncoded, etext)
    text_n = ITlib.decode(code, etext)                              # decode the text
    print "Decoded text: " + text_n
    print "Compression ratio: %.2f" % (float(LenBits) / LenBitsEncoded)
