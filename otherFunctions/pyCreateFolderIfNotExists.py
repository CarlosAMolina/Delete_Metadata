#!/usr/bin/python

from pyCheckFolderExists import pyCheckFolderExists
from pyCommandLine import pyCommandLine

def pyCreateFolderIfNotExists(newFolderPath, folderName):
	if pyCheckFolderExists(newFolderPath, folderName) == -1:
		foderPathAndName = newFolderPath+'/'+folderName
		command = ['mkdir',foderPathAndName]
		print 'New folder has been created: '+str(folderName)
		pyCommandLine(command)