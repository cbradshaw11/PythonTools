array = [1, 4, 5, 17, 9, 15, 27, 2, 3, 25]

def recursiveSort(l):
  print(l)
  if len(l) == 1:
    return l
  else:
    #print("sorting left")
    size = len(l)
    mid = int(size/2)
    left = l[0:mid]
    recursiveSort(left)
 
   # print("sorting right")
    #sort right side
    right = l[mid:]
    recursiveSort(right)


    print("left : ")
    print(left)
    print("right : ")
    print(right)

    #merge
    #i = 0
    r = 0
    j = 0
    new = []
    while j < len(left) and r < len(right):
      if left[j] > right[r]:
        new.append(left[j])
        j += 1
        if j >= len(left):
          new.extend(right)
          break
      else:
        new.append(right[r])
        r += 1
        if r >= len(right):
          new.extend(left)
          break
    
    print("new array:")
    print(new)
    l = new
    print("new l : ")
    print(l)

tmp = array
recursiveSort(tmp)

print(tmp)


 
