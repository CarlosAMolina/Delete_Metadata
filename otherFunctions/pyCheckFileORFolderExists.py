#!/usr/bin/python

import os

def pyCheckFileORFolderExists(path, name, folderORfile):
	# variables
	# input:
	# - path: string. path of the folder or file to study
	# - name: string. name of the folder or file to study
	# - folderORfile: string ('folder' or 'file'). Indicates whate to check if a folder or a file
	# output:
	# - 1: exists
	# - -1: doesn't exist
	pathAndName = path+'/'+name
	if folderORfile == 'folder':
		exists = os.path.isdir(pathAndName) # True or False
	elif folderORfile == 'file':
		exists = os.path.isfile(pathAndName) # True or False
	if exists == True: 
		return 1
	elif exists == False:
		return -1
