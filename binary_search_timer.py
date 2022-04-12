import time
import random

n = 100
array = list(range(n))

def binary_search(key):
  global array
  len_array = len(array)
  start = 0
  end = len_array - 1
  while True:
    if start == end:
      return array[start] == key
    mid = (start + end) // 2
    if array[mid] == key:
      return True
      break
    elif array[mid] > key:
      end = mid - 1
    else:
      start = mid + 1

full_time = 0
for i in range(n):
  random_int = random.randint(0, n - 1)
  start = time.time()
  binary_search(random_int)
  end = time.time()
  full_time += end - start

print(full_time / n)
