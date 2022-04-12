import random

idx = 0
array = list(range(100000))
random.shuffle(array)

idx = 0
key = int(input())

for i in array:
  if i == key:
    print("%d found at %d" % (key, idx))
    break
  idx += 1

if idx == len(array):
    print("404 Not Found")
