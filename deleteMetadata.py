#!/usr/bin/python
__author__ = 'Carlos A. Molina - @CarlosAMoli'

import sys
import os
scriptPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scriptPath+'/otherFunctions') # add folder to path to use its functions
from os import listdir
from os.path import isfile, join
from otherFunctions import *
from pyCheckFileORFolderExists import pyCheckFileORFolderExists
from pyConvert2List import pyConvert2List
from pyCreateFolderIfNotExists import pyCreateFolderIfNotExists
from pyDeleteCommasPath import pyDeleteCommasPath
from pyDeleteFilesMetadata import pyDeleteFilesMetadata
from pyDeleteFileMetadata import pyDeleteFileMetadata
from pyDeleteFiles import pyDeleteFiles
from pyGetArchivesNameInPath import pyGetArchivesNameInPath
from pyGetFilesNameInPath import pyGetFilesNameInPath
from pyGetImageNameFromPathAndName import pyGetImageNameFromPathAndName
from pyMoveFiles import pyMoveFiles

########################################################################
# delete metadata for all files (or only one) in indicated folder
# original files are moved to 'originalImages' folder or are deleted
########################################################################

# functions

def ask4DeleteOption():
	optionMetadata = ""
	while optionMetadata == "":
		optionMetadata = raw_input('Delete metadata of all files in a folder (1) or only one image (2)?\n>>> ')
		if optionMetadata == str(1) or optionMetadata == str(2):
			return int(optionMetadata)
		else:
			optionMetadata = ""

def ask4FolderPath():
	folderPath = ""
	while folderPath == "":
		folderPath = raw_input('Complete route of the folder with images (/../../..) or to the image:\n>>> ')
	return folderPath

def ask4ImageName():
	imageName = ""
	while imageName == "":
		imageName = raw_input('Complete name of the image:\n>>> ')
	return imageName

def ask4MoveORdelete():
	optionMoveORdelete = ""
	while optionMoveORdelete == "":
		optionMoveORdelete = raw_input('Save and move original files to a folder (1) or delete them (2)?\n>>> ')
		if optionMoveORdelete == str(1) or optionMoveORdelete == str(2):
			return int(optionMoveORdelete)
		else:
			optionMoveORdelete = ""

def moveORdeleteOriginalFiles(folderPath,filesName,deleteMetadataResults):
	# move orignal images with metadata or delete it
	# initialice variables
	filesOriginal = [] # original images. Images with metadata. Their matadata had been deleted and new images without metadata have been created
	folder2moveName = 'originalImages' # name of the folder where to save original images
	folder2movePath = ''
	# save files
	for index, result in enumerate(deleteMetadataResults):
		if result == 1: # work only with modified images
			fileNoMetadata = filesName[index]
			filesOriginal.append(fileNoMetadata + '_original') # when deleting metadata, original files (images with metadata) are saved as old name + _original at the end
	# move or delete
	optionOriginalFiles = ask4MoveORdelete()
	if optionOriginalFiles == 1: # move original images
		pyCreateFolderIfNotExists(folderPath, folder2moveName) # create folder where move the images
		folder2movePath = folderPath+folder2moveName
		pyMoveFiles(folderPath,filesOriginal,folderPath,folder2moveName)
		print 'Files moved to originalImages folder'
	elif optionOriginalFiles == 2:
		pyDeleteFiles(folderPath,filesOriginal)

def checkFolderPathSyntax(archivesInPath, optionMetadata, folderPath):
	# check if the folder path is correct. If the option is for working with only one image, this method checks if the images exists
	error = -1
	if allArchivesInPath != -1:
		return 1
	else:
		if optionMetadata == 2: # work with only one image
			imageExists = checkImageExists(folderPath, None)
			if imageExists == 1:
				return [1,1]
			else:
				error = 1
		else:
			error = 1
	if error == 1:
		print 'ERROR: folder path invalid syntax'
		return -1

def checkAnyArchive(archivesInPath):
	if allArchivesInPath != []:
		return 1
	else:
		print 'ERROR: folder is empty, no images'
		return -1

def checkImageExists(imagePath,imageName):
	if pyCheckFileORFolderExists(imagePath,imageName,'file') == -1:
		print "ERROR: image doesn't exist"
		return -1
	else:
		return 1


# main #
########

# delete metadata of all images in a folder or only one image

allFilesName = []
deleteMetadataResults = [] # know when metadata has been deleted
continueDeletingMetadata = "" # know if some error occurs
imageNameInPath = "" # folder's path contains the image name

optionMetadata = ask4DeleteOption()

# folder with image or images
folderPath = ask4FolderPath()
folderPath = pyDeleteCommasPath(folderPath) # '/usr/desktop' -> usr/desktop

allArchivesInPath = pyGetArchivesNameInPath(folderPath)
continueDeletingMetadata = checkFolderPathSyntax(allArchivesInPath, optionMetadata, folderPath)
if len(pyConvert2List(continueDeletingMetadata)) == 2: # len(intType) = error -> list type is necessary
	imageNameInPath = 1
	continueDeletingMetadata = 1 # [1,1] -> 1
if continueDeletingMetadata == 1:
	continueDeletingMetadata = checkAnyArchive(allArchivesInPath)
	if continueDeletingMetadata == 1:
		if optionMetadata == 1:
			allFilesName = pyGetFilesNameInPath(folderPath,allArchivesInPath) # get only files
			# delete metadata
			deleteMetadataResults = pyDeleteFilesMetadata(folderPath,allFilesName) # save when file metadata was deleted correctly
		elif optionMetadata == 2:
			if imageNameInPath == 1:
				imageNameAndPath = folderPath
				folderPath, imageName = pyGetImageNameFromPathAndName(imageNameAndPath)
				# continueDeletingMetadata checked for this case before
			else:
				imageName = ask4ImageName()
				continueDeletingMetadata = checkImageExists(folderPath, imageName)
			if continueDeletingMetadata == 1:
				continueDeletingMetadata = pyDeleteFileMetadata(folderPath, imageName)
			if continueDeletingMetadata == 1:
				deleteMetadataResults = pyConvert2List(continueDeletingMetadata)
				allFilesName.append(imageName)
if 1 not in deleteMetadataResults: # no file has been changed
	print 'No file has been changed'
	continueDeletingMetadata = -1
if continueDeletingMetadata != -1:
	moveORdeleteOriginalFiles(folderPath,allFilesName,deleteMetadataResults)
print 'Process completed'