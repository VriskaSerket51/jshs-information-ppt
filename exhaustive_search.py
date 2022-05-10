import time
import random
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.setrecursionlimit(15000)

def remove_outliers(arr):
  q1, q3 = np.percentile(arr, [25, 75])
  iqr = q3 - q1
  lower_bound = q1 - (iqr * 1.5)
  upper_bound = q3 + (iqr * 1.5)
  for value in arr:
    if value > upper_bound or value < lower_bound:
      arr.remove(value)

loops = 200
n = 1000
x = list(range(1, n + 1))
y = []

for max in x:
  spans = []
  for i in range(loops):
    start = time.time()
    _sum = 0
    for i in range(1, max + 1):
      if n%i==0:
        _sum += i
    span = time.time() - start
    spans.append(span)
  remove_outliers(spans)
  y.append(sum(spans) / len(spans))
plt.title('O(n)')
plt.plot(x, y)
