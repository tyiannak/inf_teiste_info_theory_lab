import ITlib, numpy
import matplotlib.pyplot as plt
n1 = 3; n2 = 5; n3 = 7; n4 = 9                      # number of code bits
es = numpy.arange(0, 1+0.01, 0.01)                  # bit error probability range (0 to 1 with 0.01 step)
Pes1 = []; Pes2 = []; Pes3 = []; Pes4 = []          # coding error probabilities
for e in es:                                        # for each bit error probability compute:
    Pes1.append(ITlib.repetitionCodeError(n1, e))   # coding probability for n1 code bits
    Pes2.append(ITlib.repetitionCodeError(n2, e))   # coding probability for n2 code bits
    Pes3.append(ITlib.repetitionCodeError(n3, e))   # coding probability for n3 code bits
    Pes4.append(ITlib.repetitionCodeError(n4, e))   # coding probability for n4 code bits
fig, ax = plt.subplots()                            # plot results
plt.plot(es, Pes1, label = "n=3", linewidth=2.0)
plt.plot(es, Pes2, label = "n=5", linewidth=2.0)
plt.plot(es, Pes3, label = "n=7", linewidth=2.0)
plt.plot(es, Pes4, label = "n=9", linewidth=2.0)
ax.grid(True)
plt.xlabel("e")
plt.ylabel("Pe")
legend = ax.legend(loc='upper left', shadow=True)
plt.show()