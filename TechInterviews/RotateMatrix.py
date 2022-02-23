
m = [[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15]
]

print(m)

newm = [ [ 0 for i in range(len(m)) ] for j in range(len(m[0])) ] 

print(newm)

for i in range(len(m)):
  for j in range(len(m[0])):
    newm[j][i] = m[i][j]
print(newm)

for i in newm:
  i.reverse()

print(newm)
