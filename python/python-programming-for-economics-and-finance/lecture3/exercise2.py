import numpy as np
import matplotlib.pyplot as plt

alphas = [0, 0.8, 0.98]
T = 200
ts = np.empty(T+1)


for alpha in alphas:
    ts[0] = 0
    for t in range(T):
        ts[t+1] = alpha*ts[t] + np.random.randn()
    plt.plot(ts, label=f'$\\alpha={alpha}$')
plt.legend()
plt.show()
