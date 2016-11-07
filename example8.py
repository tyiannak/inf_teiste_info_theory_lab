import ITlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

SNRdb = np.arange(0, 50, 2.5)           # snr range in db
SNR = ITlib.SNR_db_to_num(SNRdb)        # snr (num)
B = np.arange(0.1,  10,  0.1)           # bandwidth

SNR, B = np.meshgrid(SNR, B)            # meshgrid
C = ITlib.computeChannelCapacityAWGN(B, SNR)    # capacity

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(B, 10.0*np.log10(SNR), C, 
    rstride=1, cstride=1, cmap=cm.coolwarm, 
    linewidth=0, antialiased=False)
plt.xlabel("B (MHz)")
plt.ylabel("SNR (db)")
plt.title("Capacity for different bandwidths and SNRs")
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

