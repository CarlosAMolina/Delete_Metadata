#!/usr/bin/python

from pyRetrieveFilesOfType import pyRetrieveFilesOfType
from pyDeleteFileMetadata import pyDeleteFileMetadata

def pyDeleteFilesMetadata(filePath=None, filesName=None, type2delete=None):
	# variables
	# input. filePath: str. filesName: list of str (if not it is converted). type2delete: list of str (if not it is converted)
	# output: list of ints
	filesName = pyRetrieveFilesOfType(filePath,filesName,type2delete) # list
	deleteFiles = [] # check if any error occurs
	for fileName in filesName:
		deleteFiles.append(pyDeleteFileMetadata(filePath, fileName))
	return deleteFiles