array = list(range(100000))
len_array = len(array)
idx = 0
key = int(input())

start = 0
end = len_array - 1

while True:
  if start == end:
    print("404 Not Found")
    break
  mid = (start + end) // 2
  if array[mid] == key:
    print("Found %d at %d" % (key, mid));
    break
  elif array[mid] > key:
    end = mid - 1
  else:
    start = mid + 1
