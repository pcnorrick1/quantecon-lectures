import numpy as np

num_sims = 100000

inside = 0
outside = 0

for i in range(num_sims):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    dist = np.sqrt(x**2 + y**2)
    if dist <1:
        inside = inside+1
    else:
        outside = outside+1
    i+=1

total = inside + outside

pi = 4*inside/total
print(pi)

