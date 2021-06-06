import time
import numpy as np
from matplotlib import pyplot as plt, colors as mcolors, cm

timeStart = time.time()

# objectCoordsByFreqNoType
# firstObjectCoordsByFreq
# objectCoords
# firstObjectCoords

print('Reading...')

# with open('scripts/out/firstObjectCoords.csv', 'r') as f:
#   next(f)
#   lines = f.readlines()

with open('scripts/out/objectCoords.csv', 'r') as f:
  next(f)
  lines = f.readlines()

data = [line.split(',') for line in lines]

x = [float(i[0]) for i in data]
y = [float(i[1]) for i in data]
lines = []

print('Data read, plotting...')

hist = plt.hist2d(
  x,
  y,
  bins=[64, 48],
  range=[[0, 512], [0, 384]],
  density=True,
  cmap=cm.jet,
  norm=mcolors.PowerNorm(0.275)
)

plt.axis('image')
plt.gca().xaxis.set_ticks_position('top')
plt.gca().invert_yaxis()

cb = plt.colorbar(hist[3])
cb.set_label('PowerNorm(0.275)')

print('Plotted in {}'.format(time.time() - timeStart))
plt.show()

# x = [float(x) for x, y, n in data]
# y = [float(y) for x, y, n in data]
# n = [float(n) for x, y, n in data]
# data = []

# print('Data read, building plot...')

# hex = plt.hexbin(x, y, n, gridsize=(128, 96), bins='log', mincnt=10, cmap=cm.bwr)
# plt.axis('image')
# plt.gca().invert_yaxis()

# cb = plt.colorbar(hex)
# cb.set_label('log10(objects)')

# plt.show()
# print('Finished in {}'.format(time.time() - timeStart))
