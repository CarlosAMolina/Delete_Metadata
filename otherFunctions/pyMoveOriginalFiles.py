#!/usr/bin/python

from pyCommandLine import pyCommandLine

def pyMoveOriginalFiles(filesPath, filesName, folder2movePath, folder2moveName):
	# variables
	# input. filesPath: str, filesName: list of str, folder2movePath: str, folderName2move: str
	# output: str
	folderNameAndPath = folder2movePath+'/'+folder2moveName
	for fileName in filesName:
		fileNameAndPath = filesPath+'/'+fileName
		command = ['mv', fileNameAndPath, folderNameAndPath]
		pyCommandLine(command)