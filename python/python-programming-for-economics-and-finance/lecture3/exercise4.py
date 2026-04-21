import numpy as np
import matplotlib.pyplot as plt

T = 200
alpha = 0.9

ts = np.empty(T+1)
ts[0] = 0
for t in range(T):
    if ts[t] < 0:
        ts_new = -1*ts[t]
    else:
        ts_new = ts[t]
    ts[t+1] = alpha*ts_new + np.random.randn()

plt.plot(ts)
plt.show()

