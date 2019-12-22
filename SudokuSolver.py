#Sudoku Solver

import sys

matrix = [0]*9
for i in range(0,9):
	matrix[i] = [i]*9

OGmatrix = [0]*9
for i in range(0,9):
	OGmatrix[i] = [i]*9

def PrintBoard(m):
	for i in range(0,9):
		for j in range(0,9):
			sys.stdout.write(str(m[i][j]))
		sys.stdout.write("\n")

def OutputBoard(m):
	file = open("output.txt",'a')
	for i in range(0,9):
			for j in range(0,9):
				file.write(str(m[i][j]))
			file.write("\n")

def TextOut(s):
	file = open("output.txt",'a')
	file.write(s)
	file.close()

def CreateOutputFile():
	file = open("output.txt",'w')

def PrintRow(RowNum):
	print(matrix[RowNum-1])

def PrintCol(ColNum):
	for i in range(0,9):
		print(matrix[i][ColNum-1])

def FillBoard(lists, m):
	x = 0
	for list in lists:
		y = 0
		for char in list:
			if(char == '\n'):
				continue
			m[x][y] = int(char)
			y+=1
		x+=1

def ReadBoard(m):
	file = open("hello.txt", "r")
	list = file.readlines()
	FillBoard(list,m)

def CreateTmpBoard():
	global matrix
	for i in range(0,9):
		for j in range(0,9):
			matrix[i][j] = OGmatrix[i][j]

def CheckRow(RowNum):
	global matrix
	return CheckList(matrix[RowNum-1])


def CheckCol(ColNum):
	global matrix
	list = [None]*9
	for i in range(0,9):
		list[i] = matrix[i][ColNum-1]
	return CheckList(list)

def CheckList(list):
	tmplist = []
	for num in list:
		if num == 0:
			continue
		else:
			if num in tmplist:
				return -1
			else:
				tmplist.append(num)
	return 1

def CheckSquare(x,y):
	list = [None]*9
	rowsec = (x-1)/3
	colsec = (y-1)/3

	tmplist = []
	for i in range(3*rowsec, 3*rowsec + 3):
		for j in range(3*colsec, 3*colsec + 3):
			if(matrix[i][j] == 0):
				continue
			if(matrix[i][j] in tmplist):
				return -1
			else:
				tmplist.append(matrix[i][j])
	return 1

def TripleCheck(x,y):
	a = CheckRow(x)
	b = CheckCol(y)
	c = CheckSquare(x,y)
	if(a == 1 and b == 1 and c == 1):
		return 1
	else:
		return 0

def CheckBoard():
	global matrix
	for i in range(1,10):
		for j in range(1,10):
			if(TripleCheck(i,j)):
				print("Good!")
			else:
				print("Bad..")

#returns list of all possible nums that can go in square based on OG
def PossibleList(x,y):

	if OGmatrix[x-1][y-1] != 0:
		TextOut(str(x)+","+str(y)+" Already filled...exiting\n")
		return []

	localrowlist = []
	localcollist = []
	localsquarelist = []
	PossibleList = []
	rowsec = (x-1)/3
	colsec = (y-1)/3

	for i in range(0,9):
		if OGmatrix[x-1][i] != 0:
			localrowlist.append(OGmatrix[x-1][i])
	for i in range(0,9):
		if OGmatrix[i][y-1] != 0:
			localcollist.append(OGmatrix[i][y-1])
	for i in range(3*rowsec, 3*rowsec + 3):
		for j in range(3*colsec, 3*colsec + 3):
			if OGmatrix[i][j] != 0:
				localsquarelist.append(OGmatrix[i][j])

	for i in range(1,10):
		if i not in localrowlist:
			if i not in localcollist:
				if i not in localsquarelist:
					PossibleList.append(i)
	TextOut("Possible nums: ")
	for i in PossibleList:
		TextOut(str(i)+" ")
	TextOut("\n")
	return PossibleList


def Solver(x,y):
	TextOut("Beginning of Function at "+str(x)+","+str(y)+"\n")
	global matrix
	global OGmatrix

	if OGmatrix[x-1][y-1] != 0:
		if x < 9:
			TextOut("Already filled...calling solver func 1\n\n")
			Solver(x+1,y)
			return
		elif y < 9:
			TextOut("Already filled...calling solver func 2\n\n")
			Solver(1,y+1)
			return
		else:
			PrintBoard(matrix)
			TextOut("DONE")
			exit()

	localpossibilities = PossibleList(x,y)

	OutputBoard(matrix)
	for i in localpossibilities:
		TextOut("Trying ["+str(i)+"] at square ("+str(x)+","+str(y)+")\n")
		matrix[x-1][y-1] = i
		if TripleCheck(x,y):
			OutputBoard(matrix)
			if x < 9:
				TextOut("That worked..calling solver func 3\n\n")
				Solver(x+1,y)
			elif y < 9:
				TextOut("That worked..calling solver func 4\n\n")
				Solver(1,y+1)
			else:
				TextOut("Puzzle Solved...\n\n")
				PrintBoard(matrix)
				exit()
		else:
			matrix[x-1][y-1] = 0
			TextOut(str(i)+" failed...moving to next possible number\n")
	matrix[x-1][y-1] = 0
	TextOut("End of Func...Returning to caller\n\n")



CreateOutputFile()
ReadBoard(OGmatrix)
ReadBoard(matrix)

#print(PossibleList(7,1))

Solver(1,1)
