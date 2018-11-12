import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(8,6))
fig.add_subplot(231).hist(np.random.randn(100),bins=20, color='k',alpha=0.3)
fig.add_subplot(233).scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))
fig.add_subplot(235).plot(np.arange(10))
fig.add_subplot(232).bar(np.arange(10), np.arange(10))
fig.add_subplot(234).plot(np.sin(np.linspace(-np.pi, np.pi,256)))
fig.add_subplot(236).plot(np.arange(10))

plt.show()