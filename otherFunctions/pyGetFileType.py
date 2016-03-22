#!/usr/bin/python

from pyCommandLine import pyCommandLine
import re

def pyGetFileType(filePath=None,fileName=None):
	
	# use:
	# from pyGetFileType import pyGetFileType; pyGetFileType()
	# variables:
	# input. fileName: str, filePath: str
	# output:list

	fileNameAndPath = filePath+'/'+fileName # name showed in folder

	# fyle Type (FT)
	# command line: file --mime-type -b foto2
	FTcommand='file'
	FTarg1='--mime-type'
	FTarg2='-b'
	FTarg3= fileNameAndPath
	command=[FTcommand,FTarg1,FTarg2,FTarg3]

	# execute
	commandResults = pyCommandLine(command)

	# separate info, create a list
	fileType = re.compile('/').split(commandResults)

	return fileType