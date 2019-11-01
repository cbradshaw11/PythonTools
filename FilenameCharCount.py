
########################################################
# Title: FilenamCharCount.py                           #
# Purpose: This Script was written to find any files   #
# with a path name that was over 100 characters long   #
# Usage: FilenamCharCount.py [StartPath] [MaxLength]   #
########################################################

import os
import sys

maxlength = 100

def countChars(path):
	return len(path)

def search():
	for file in os.listdir():
		if('.' in file):
			dir_path = os.path.dirname(os.path.realpath(file))
			charlength = countChars(dir_path+file)
			if (charlength > maxlength):
				print("   "+dir_path+file+" : "+charlength)
		else:
			os.chdir(file)
			search()
	os.chdir('..')
	return

def main():
	if(len(sys.argv) == 2):
		try:
			print("Running Search on "+sys.argv[1])
			os.chdir(sys.argv[1])
		except:
			print("Directory provided does not exist or was not typed correclty...exiting program")
			exit(0)
	if(len(sys.argv) > 2):
		maxlength = sys.argv[2]
	search()
	
if __name__ == '__main__' :
	main()