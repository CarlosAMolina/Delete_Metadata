#!/usr/bin/python

from pyCommandLine import pyCommandLine

def pyDeleteFile(fileName):
	# variables
	# input: str (can be only te fileName or filePath+'/'+fileName)
	# output: str
	command = ['rm',str(fileName)]
	return pyCommandLine(command)