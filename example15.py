import ITlib

charCounts = {"a":50, "b":12, "c":11, "d":80, "e":38}
text = "cacabeecdad"
print "Initial text: " + text
huffCode, length = ITlib.generateHuffmanCode(charCounts)        # generate huffman code
etext = ITlib.encode(huffCode, text)                            # encode using huffman code
etext = "".join(etext)                                          # convert list to string
print "Encoded text " + etext
text_n = ITlib.decode(huffCode, etext)                          # decode the text
print "Decoded text: " + text_n
