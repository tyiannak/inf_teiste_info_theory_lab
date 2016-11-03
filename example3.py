import ITlib
import numpy
import os
import cv2
import matplotlib.pyplot as plt

def computeImageEntropy(path):
    RGB = cv2.imread(path, cv2.CV_LOAD_IMAGE_COLOR)                 # read an image from a jpg file
    Grayscale = cv2.cvtColor(RGB, cv2.cv.CV_RGB2GRAY)               # convert to grayscale (2D)
    countValues = numpy.zeros((256,))                               # inialize histogram (counter for each 0..255 pixel value)
    for i in range(Grayscale.shape[0]):                             # for each row i
        for j in range(Grayscale.shape[1]):                         # for each collumn j
            countValues[Grayscale[i,j]] += 1                        # increase the respective grayscale value
    countValues /= countValues.sum()                                # normalize by sum()
    H = ITlib.computeEntropy(countValues)                           # compute entropy 
    return H, Grayscale                                             # return entropy and grayscale

print "\nExample 3"
print "Compute the entropy of three gray-scale images\n"
H1, I1 = computeImageEntropy("data" + os.sep + "dot.jpg")
H2, I2 = computeImageEntropy("data" + os.sep + "seaGray.jpg")
H3, I3 = computeImageEntropy("data" + os.sep + "cityGray.jpg")
H4, I4 = computeImageEntropy("data" + os.sep + "noiseGray.jpg")
Hmax = ITlib.computeMaxEntropy(256)

plt.subplot(2,2,1);
plt.imshow(I1, cmap='Greys_r')
plt.title('H = %.2f, P = %.1f%%' % (H1, 100*(1.0-H1/Hmax)))
plt.subplot(2,2,2);
plt.imshow(I2, cmap='Greys_r')
plt.title('H = %.2f, P = %.1f%%' % (H2, 100*(1.0-H2/Hmax)))
plt.subplot(2,2,3);
plt.imshow(I3, cmap='Greys_r')
plt.title('H = %.2f, P = %.1f%%' % (H3, 100*(1.0-H3/Hmax)))
plt.subplot(2,2,4);
plt.imshow(I4, cmap='Greys_r')
plt.title('H = %.2f, P = %.1f%%' % (H4, 100*(1.0-H4/Hmax)))
plt.show()
