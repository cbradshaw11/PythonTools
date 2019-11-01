import os

print (type(os.environ['PATH']))
str = os.environ['PATH']
p = str.split(';')
for s in p:
	print(s)
while(1):
	i=1