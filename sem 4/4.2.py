import matplotlib.pyplot as plt
import numpy as np

pos = 0
scale = 10
size = 5000
values = np.random.normal(pos, 10, size)
plt.hist(values, 100)
ize = 1000
values = np.random.normal(pos, 10, ize)
plt.hist(values, 100)
ze = 500
values = np.random.normal(pos, 10, ze)
plt.hist(values, 100)

plt.show()
