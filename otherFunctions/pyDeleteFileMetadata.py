#!/usr/bin/python

from pyCommandLine import pyCommandLine

# Note: if metadata of the image had been removed before, now the file won't be modified

def pyDeleteFileMetadata(filePath, fileName):
	# variables
	# input. filePath: str. fileName: str
	# output: int
	try:
		fileNameAndPath = filePath+'/'+fileName
		command = ['exiftool', '-all=',str(fileNameAndPath)]
		result = pyCommandLine(command)
		if 'imagefilesunchanged' in result: # if the metadatas were removed previously, the file won't be modified
			print 'WARNING: file ' + str(fileName) + " doesn't change (metadata must be already deleted)"
			return -1
		else:
			return 1
	except:
		print 'ERROR delete metadata. File: ' + str(fileName)
		return -1