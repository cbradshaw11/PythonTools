def changelist(l):
  newlist = [4,3,2,1]
  l = newlist

def changelist2(l):
  newlist = [4,3,2,1]
  for i in range(len(l)):
    l[i] = newlist[i]

ll = [1,2,3,4]
changelist2(ll)
print(ll)
