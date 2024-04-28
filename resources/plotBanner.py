import numpy as np
import matplotlib.pyplot as plt

A = np.load("plane_XZ_T_2250.npy")
A -= np.mean(A)

figSize = (24, 6)
fig = plt.figure(figsize=figSize)
ax = fig.add_subplot(1, 1, 1)

X = np.linspace(-2, 2, A.shape[0])
Z = np.linspace( 0, 1, A.shape[1])
im = ax.contourf(X, Z, A.transpose(), cmap='bwr', vmin=-0.05, vmax=0.05, levels=500)

plt.axis('off')
fig.axes[0].get_xaxis().set_visible(False)
fig.axes[0].get_yaxis().set_visible(False)
plt.savefig('newBanner.png', bbox_inches='tight', pad_inches = 0)
