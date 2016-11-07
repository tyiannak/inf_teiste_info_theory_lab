import ITlib
import numpy
import matplotlib.pyplot as plt
print "\nExample 6"
print "SNR num-db relationshio\n"
SNR1 = numpy.arange(0.01, 10, 0.01)     # low values
SNR2 = numpy.arange(10,2000,10)         # higher values
SNRdb1 = ITlib.SNR_num_to_db(SNR1)      # convert to db
SNRdb2 = ITlib.SNR_num_to_db(SNR2)      # convert to db
plt.subplot(2,1,1)                      # plot
plt.plot(SNR1, SNRdb1)
plt.xlabel("SNR")
plt.ylabel("SNR (db)")
plt.subplot(2,1,2)
plt.plot(SNR2, SNRdb2)
plt.xlabel("SNR")
plt.ylabel("SNR (db)")
plt.show()
