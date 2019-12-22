import os
import socket   
import sys 
import getpass
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

processList = []
processDataList = []
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)



#r = os.popen('tasklist /S /v').read().strip().split('\n')
#print ('# of tasks is %s' % (len(r)))


#for x in range(len(r)):
#	tmpi = 0
#	tmpbool = 0
#	for i in range(len(r[x])):
#		if tmpbool:
#			tmpi = i
#		if(r[x][i] == " "):
#			if tmpbool == 0:
#				processDataList.append(r[x][tmpi:i])
#				tmpbool = 1
#		else:
#			tmpbool = 0
#	processList.append(processDataList[:])
#	processDataList.clear()
#print("\n")	
#print (processList[0])
#
#for x in range(len(processList)):
#	print(processList[x][0])
