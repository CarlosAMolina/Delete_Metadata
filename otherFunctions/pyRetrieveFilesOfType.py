#!/usr/bin/py

from pyConvert2List import pyConvert2List
from pyGetFileType import pyGetFileType
from pyCheckAnyInList import pyCheckAnyInList

def pyRetrieveFilesOfType(filesPath, files2studyName, filesType2search=None):
	# retrieve files name of indicated types
	# variables
	# input:
	# filesType2search: list of types to search (if no a list the script converts to one)
	# filesPath: route of the files to study
	# files2studyName: name of the files to analyze type.
	# output
	# filesOfType: list. Name of the files of the indicated types
	# examples
	# - .py: x-python
	# - .png: png
	filesOfType = [] # save files name of the indicated type
	if filesType2search == None: # retrieve all files
		filesOfType = files2studyName
		# filesOfType = [file for file in files2studyName if isfile(join(filesPath,file))] # files
		# filesOfType = listdir(imagesPath) # all archives, example: folders, files, etc
	else:
		#[f for f in allfiles if pyCheckAnyInList(pyGetFileType(f+'/'+imagesPath),'png')==1]
		filesType2search = pyConvert2List(filesType2search)
		for file2studyName in files2studyName:
			fileType = pyGetFileType(filesPath,file2studyName)
			fileType = pyConvert2List(fileType) # list neccesary for pyCheckAnyInList
			for fileType2search in filesType2search:
				if pyCheckAnyInList(fileType, fileType2search) == 1:
					filesOfType.append(file2studyName)
	return filesOfType
