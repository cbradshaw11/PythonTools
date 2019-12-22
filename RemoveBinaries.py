
########################################################
# Title: RemoveBinaries.py                           #
# Purpose: This Script was written to find any files   #
# with a path name that was over 100 characters long   #
# Usage: FilenamCharCount.py [StartPath] [MaxLength]   #
########################################################

import os
import sys
import shutil
from stat import S_IREAD, S_IRGRP, S_IROTH


BinaryList = [
'jpg','png','gif','bmp', 'tiff','psd',
'mp4','mkv','avi','mov','mpg','vob',
'mp3','aac','wav','flac','ogg','mka','wma',
'pdf','doc','xls','ppt','docx','odt',
'zip','rar','7z','tar','iso',
'mdb','accde','frm','sqlite',
'exe','dll','so','class','a','lib','shd'
'ico','sd','log','stg','o','su','bin','st','lst','romfs',
'pyc','pkh','pri','pub','out','romLoad','sfs','vxe','rlHeader','rlPayload','csf',
'img','err'
]

def changeperms(file):
	os.chmod(file, 644)

def RecChangePerms():
	for file in os.listdir():
		if (os.path.isdir(file)):
			os.chdir(file)
			RecChangePerms()
		else:
			changeperms(file)
	os.chdir('..')
	
	
def extensions(file):
	extenlist = file.split('.')
	if(len(extenlist) > 2):
		print(file)
	elif(len(extenlist) == 2 and extenlist[1] in BinaryList):
		try:
			os.remove(file)
		except:
			try:
				changeperms(file)
				os.remove(file)
			except:
				print("Could not change permissions and delete the following: "+file)
				return

def search():
	for file in os.listdir():
		if(file == 'lost+found'):
			os.chdir(file)
			RecChangePerms()
			shutil.rmtree(file)
			continue
		if(os.path.isdir(file)):
			os.chdir(file)
		else:
			print("Tried switching dirs to "+os.getcwd()+"/"+file)
			continue
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