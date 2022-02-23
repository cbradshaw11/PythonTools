array = [2,5,1,9,7,16,25]

def mergesort(l):
  if len(l) == 1:
    return
  
  mid = int(len(l)/2)
  left = l[:mid]
  right = l[mid:]

  mergesort(left)
  mergesort(right)

  i = j = k = 0
  while i < len(left) and j < len(right):
    if left[i] > right[j]:
      l[k] = left[i]
      i+=1
    else:
      l[k] = right[j]
      j+=1

    k+=1

  while i < len(left):
    l[k] = left[i]
    i+=1
    k+=1
  while j < len(right):
    l[k] = right[j]
    j+=1
    k+=1


tmp = array
mergesort(tmp)

print(tmp)


