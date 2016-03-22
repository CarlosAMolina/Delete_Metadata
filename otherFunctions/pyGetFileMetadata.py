#!/usr/bin/python

from pyConvert2List import pyConvert2List
from pyCommandLine import pyCommandLine

def pyGetFileMetadata(filePath=None, filesName=None):
	# variables
	# input. filePath: str. filesName: list of str (if not it is converted)
	# output: str
	filesName = pyConvert2List(filesName)
	metadatas = []
	for fileName in filesName:
		fileName = filePath+'/'+fileName
		command = ['exiftool', str(fileName)]
		metadata = pyCommandLine(command)
		metadatas.append(metadata)
	return metadatas