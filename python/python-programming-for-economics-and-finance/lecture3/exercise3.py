import numpy as np
import matplotlib.pyplot as plt

T = 200
alpha = 0.9

ts = np.empty(T+1)
ts[0] = 0
for t in range(T):
    ts[t+1] = alpha*np.abs(ts[t]) + np.random.randn()

plt.plot(ts)
plt.show()

