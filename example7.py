import ITlib

print "\nExample 7"
print "1000 videos (1080x720,RGB,25fps) are transmitted in a 60db SNR channel."
print "Available Bandwidth is 1MHz. What is the required compression ratio?\n"

B = 10.0 ** 6
SNRdb = 60

Width = 1080
Height = 720
nChannels = 3
fps = 25
bitsPerSample = 8
R = Width * Height * nChannels * fps * bitsPerSample
SNR = ITlib.SNR_db_to_num(SNRdb)
C = ITlib.computeChannelCapacityAWGN(B, SNR)

print "SNR = %.1f db is equivalent to %.1f" % (SNRdb, SNR)
print "Information rate is %.1f bps" % R
print "Channel capacity is %.1f bps" % C
print "Required compression ratio is %.1f : 1" % (R/C)