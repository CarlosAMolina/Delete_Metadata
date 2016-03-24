#!/usr/bin/python

from pyCheckFileORFolderExists import pyCheckFileORFolderExists
from pyCommandLine import pyCommandLine

def pyCreateFolderIfNotExists(newFolderPath, folderName):
	if pyCheckFileORFolderExists(newFolderPath, folderName, 'folder') == -1:
		foderPathAndName = newFolderPath+'/'+folderName
		command = ['mkdir',foderPathAndName]
		print 'New folder has been created: '+str(folderName)
		pyCommandLine(command)