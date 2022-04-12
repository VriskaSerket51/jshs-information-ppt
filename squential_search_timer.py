import random
import time

n = 100
array = list(range(n))

def squential_search(key):
  idx = 0
  global array
  for i in array:
    if i == key:
      return True
      break
    idx += 1

  if idx == len(array):
    return False

full_time = 0
for i in range(n):
  random_int = random.randint(0, n - 1)
  start = time.time()
  squential_search(random_int)
  end = time.time()
  full_time += end - start

print(full_time / n)
