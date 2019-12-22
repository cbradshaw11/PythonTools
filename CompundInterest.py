import sys


def Compound():	
	start1 = 67000
	start2 = 70000
	currentsal1 = start1
	currentsal2 = start2
	interest = 0.05
	numyears = 30
	sum1 = 0
	sum2 = 0
	for i in range(numyears):
		tmpsal1 = currentsal1 + (currentsal1*interest)
		difference1 = tmpsal1 - currentsal1
		currentsal1 = currentsal1 + (currentsal1*interest)
		sum1 = sum1 + currentsal1
		
		tmpsal2 = currentsal2 + (currentsal2*interest)
		difference2 = tmpsal2 - currentsal2
		currentsal2 = currentsal2 + (currentsal2*interest)
		sum2 = sum2 + currentsal2
		print(str(currentsal1)+" : "+str(currentsal2)+"\n")
	
	print(sum2-sum1)


if __name__ == '__main__' :
	Compound()