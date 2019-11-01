
import sys
import os


def changeperms(file):
	os.chmod(file, 644)
	
def main():
	if(len(sys.argv) == 2):
		try:
			print("Changing permissions on "+sys.argv[1])
			os.chdir(sys.argv[1])
		except:
			print("Directory provided does not exist or was not typed correclty...exiting program")
			exit(0)
	if(len(sys.argv) > 2):
		maxlength = sys.argv[2]
	for file in os.listdir():
		changeperms(file)
	
if __name__ == '__main__' :
	main()