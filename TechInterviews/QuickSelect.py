def partition(arr, low, high):
  partition_value = arr[high]
  pi = 0

  for i in range(low, high):
    if arr[i] < partition_value:
      arr[pi], arr[i] = arr[i], arr[pi]
      pi += 1
  arr[pi], arr[high] = arr[high], arr[pi]
  return pi  


def select(arr, low, high, k):
  if low >= high:
    return arr[low]

  pi = partition(arr, low, high)
  if pi == (k-1):
    return arr[pi]
  if pi > k-1:
    return select(arr, low, pi-1, k)
  if pi < k-1:
    return select(arr, pi+1, high, k)



array = [5,1,4,2,3,9,6,8,7]
k = 3

val = select(array, 0, len(array)-1, k)
print(val)
print(array)
