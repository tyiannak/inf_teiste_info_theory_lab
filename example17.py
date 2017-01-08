import ITlib, numpy
import matplotlib.pyplot as plt
import numpy
n1 = 3
n2 = 5
n3 = 7
n4 = 9
es = numpy.arange(0, 1+0.01, 0.01)
Pes1 = []
Pes2 = []
Pes3 = []
Pes4 = []
for e in es:
    Pes1.append(ITlib.repetitionCodeError(n1, e))
    Pes2.append(ITlib.repetitionCodeError(n2, e))
    Pes3.append(ITlib.repetitionCodeError(n3, e))
    Pes4.append(ITlib.repetitionCodeError(n4, e))
fig, ax = plt.subplots()
plt.plot(es, Pes1, label = "n=3", linewidth=2.0)
plt.plot(es, Pes2, label = "n=5", linewidth=2.0)
plt.plot(es, Pes3, label = "n=7", linewidth=2.0)
plt.plot(es, Pes4, label = "n=9", linewidth=2.0)
ax.grid(True)
plt.xlabel("e")
plt.ylabel("Pe")
legend = ax.legend(loc='upper left', shadow=True)

plt.show()