import os
import sys
import shutil
from stat import S_IREAD, S_IRGRP, S_IROTH


def setuptest():
	try:
		os.mkdir('hello')
	except:
		print("directory exists")
	os.chdir('hello')
	file = open('hello.txt','w')
	file.write("hello world\n")
	os.chmod('hello.txt', S_IREAD|S_IRGRP|S_IROTH)
	
	
def main():
	if(len(sys.argv) == 2):
		try:
			print("Creating test in  "+sys.argv[1])
			os.chdir(sys.argv[1])
		except:
			print("Directory provided does not exist or was not typed correclty...exiting program")
			exit(0)
	
	setuptest()
	
if __name__ == '__main__' :
	main()