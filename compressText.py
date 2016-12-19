import ITlib, sys, bitarray, cPickle, os
if __name__ == '__main__':
    mode, inputFilePath, outputFilePath = (sys.argv[1], sys.argv[2], sys.argv[3])
    if mode == "compress":
        method = sys.argv[4]
        f = open(inputFilePath)                                         # read the input file
        text = f.read()
        f.close()
        charCounts = ITlib.getTextCountsUnique(text)                    # get character counts
        if method == "H" or method == "Huffman":
            code, length = ITlib.generateHuffmanCode(charCounts)        # generate huffman code
        elif method == "SF" or method == "Shannon-Fano":
            code, length = ITlib.generateShannonFanoCode(charCounts)    # generate shannon-fano code            
        else:
            raise ValueError('Method argument must be either Huffman\
              (or H) or Shannon-Fano (or SF)')
        etext = ITlib.encode(code, text)                                # encode using huffman code
        etext = "".join(etext)                                          # convert list to string
        etextBits = bitarray.bitarray(etext)                            # convert to bitarray type         
        with open(outputFilePath,"wb") as f:                            # write bits to binary file
            etextBits.tofile(f)        
        cPickle.dump(code, open(outputFilePath+"_code", "wb" ) )        # write code to file
        inFSize = os.stat(inputFilePath).st_size 
        outFSize =  os.stat(outputFilePath).st_size 
        codeFSize =  os.stat(outputFilePath+"_code").st_size         
        print "Original file size is %d bytes" % inFSize
        print "Compressed file size is %d bytes \
            (%d for encoded text and %d for the code itself)" % \
            (outFSize + codeFSize, outFSize, codeFSize)
        print "Compression ratio is %.3f" % \
         (float(inFSize) / (outFSize + codeFSize))
    elif mode == "uncompress":
        etextBits = bitarray.bitarray()
        with open(inputFilePath,"r") as f:                              # load bits from comrpessed file
            etextBits.fromfile(f)
        code = cPickle.load(open(inputFilePath+"_code", "r" ) )         # load code from file        
        text_n = ITlib.decode(code, etextBits.to01())                   # decode the text
        with open(outputFilePath, "w") as f:                            # write decoded text to file
            f.write(text_n)
            f.close()