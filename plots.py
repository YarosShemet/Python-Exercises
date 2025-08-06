import numpy as np
import matplotlib.pyplot as plt
x1 = [0, 900]
y1 = [900/4, 0]
x2 = [0, -15]
y2 = [6, 0]
plt.plot(x1, y1)
plt.plot(x2, y2)
idx = np.argwhere(np.diff(np.sign(f - g))).flatten()
plt.plot(x[idx], f[idx], 'ro')
plt.show()
