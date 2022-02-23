
m = [ [1,2,3,4,5],
      [6,7,8,9,10],
      [11,12,13,14,15],
      [16,17,18,19,20]
    ]

print(m)

w = len(m[0])-1
minw = 0
h = len(m)-1
minh = 1
i = 0
j = 0
goright = True
goleft = False
goup = False
godown = False
max = len(m) * len(m[0])
numiters = 0
while True:
  numiters += 1
  print(m[j][i])

  if goright:
    i += 1
    if i == w:
      goright = False
      godown = True
      w -= 1

  elif goleft:
    i -= 1
    if i == minw:
      goleft = False
      goup = True
      minw += 1 
  
  elif goup:
    j -= 1
    if j == minh:
      goup = False
      goright = True
      minh += 1
      

  elif godown:
    j += 1
    if j == h:
      godown = False
      goleft = True
      h -= 1
    
  if numiters == max:
    break




