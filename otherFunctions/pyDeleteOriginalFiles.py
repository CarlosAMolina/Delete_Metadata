#!/usr/bin/python

from pyCommandLine import pyCommandLine

def pyDeleteOriginalFiles(filePath, filesName):
	# variables
	# input. filePath: str. filesName: list of str (if not it is converted). type2delete: list of str (if not it is converted)
	# output: str
	for fileName in filesName:
		fileName = fileName + '_original' # when delete metadata, original files are saved as old name + _original at the end
		fileNameAndPath = filePath+'/'+fileName
		command = ['rm', str(fileNameAndPath)]
		pyCommandLine(command)
	