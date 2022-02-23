
def partition(arr, low, high):
  pivot = arr[high]
  pi = low
  
  for i in range(low, high):
    if arr[i] > pivot:
      arr[pi], arr[i] = arr[i], arr[pi]
      pi += 1
  arr[pi], arr[high] = arr[high], arr[pi]
  
  return pi 

def quicksort(arr, low, high):
  if len(arr) < 2:
    return
 
  if low >= high:
    return
 
  pi = partition(arr, low, high)

  quicksort(arr, low, pi-1)
  quicksort(arr, pi+1, high)


array = [5,7,4,9,1,6,8,3,2]

quicksort(array, 0, len(array)-1)

print(array)
