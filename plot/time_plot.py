import numpy as np
from matplotlib import pyplot as plt

time_ac = np.load('ac.npy')
time_ph = np.load('ph.npy')
time_ac[0] = 0
time_ph[0] = 0

linewidth = 3
stage_plot = [1, 2, 3, 4]
for i in range(len(stage_plot)):
    plt.plot(time_ph[i:i + 2], stage_plot[i] * np.ones(2), 'b', linewidth=linewidth)
for i in range(len(stage_plot)):
    plt.plot(time_ac[i:i + 2], stage_plot[i] * np.ones(2), 'r', linewidth=linewidth)
plt.grid(True)
plt.xlabel('Time (seconds)')
plt.ylabel('Stage')
plt.yticks([1, 2, 3, 4])
plt.show()
