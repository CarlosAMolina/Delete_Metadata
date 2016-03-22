#!/usr/bin/python

from pyDeleteFile import pyDeleteFile

def pyDeleteFiles(filesPath, filesName):
	# variables
	# input. filesPath: str. filesName: list of str
	# output: str
	for fileName in filesName:
		fileNameAndPath = filesPath+'/'+fileName
		print 'File deleted: ' + str(fileName)
		return pyDeleteFile(fileNameAndPath)