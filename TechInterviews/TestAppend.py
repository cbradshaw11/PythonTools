l1 = ['a','b','c']
l2 = ['d','e','f']

l1.append(l2)

print(l1)

l1[3][0] = 'g'

print(l1)

print(l2)

newlist = [1,2,3]
a = 4
newlist.append(a)
print (newlist)

newlist[3] = 5

print(newlist)

print(a)

newlist.append("hello")

print(newlist)

otherlist = [6,7,'g','h']

print(otherlist)
print(type(otherlist))

newlist.append(otherlist)

print(newlist)
print(type(newlist))

newlist[5][0] = 'x'

print(newlist)

print(otherlist)


