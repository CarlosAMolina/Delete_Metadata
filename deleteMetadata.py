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
from pyDeleteFilesMetadata import pyDeleteFilesMetadata
from pyDeleteFileMetadata import pyDeleteFileMetadata
from pyDeleteFiles import pyDeleteFiles
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

def ask4MoveORdelete():
	optionMoveORdelete = ""
	while optionMoveORdelete == "":
		optionMoveORdelete = raw_input('Save and move original files to a folder (1) or delete them (2)?\n>>> ')
		if optionMoveORdelete == str(1) or optionMoveORdelete == str(2):
			return int(optionMoveORdelete)
		else:
			optionMoveORdelete = ""


def moveORdeleteOriginalFiles(imagesPath,filesName,deleteMetadataResults):
	# move orignal images with metadata or delete it
	if len(filesName) != 0:
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
			pyCreateFolderIfNotExists(imagesPath, folder2moveName) # create folder where move the images
			folder2movePath = imagesPath+folder2moveName
			pyMoveFiles(imagesPath,filesOriginal,imagesPath,folder2moveName)
			print 'Files moved to originalImages folder'
		elif optionOriginalFiles == 2:
			pyDeleteFiles(imagesPath,filesOriginal)


# main
# delete metadata of all images in a folder or only one image

allFilesName = []
deleteMetadataResults = [] # know when metadata has been deleted
continueDeletingMetadata = "" # know if some error occurs

optionMetadata = ask4DeleteOption()
if optionMetadata == 1:
	imagesPath = raw_input('Complete route of the folder with images (/../../..):\n>>> ')
	# all files at indicated folder
	try:
		allArchivesInPath = listdir(imagesPath) # all archives, example: folders, files, etc
	except:
		continueDeletingMetadata = -1
	if continueDeletingMetadata == -1:
		print 'ERROR: images path invalid syntax'
	elif allArchivesInPath == []:
		print 'ERROR: folder is empty, no images'
		continueDeletingMetadata = -1
	else:
		allFilesName = [file for file in allArchivesInPath if isfile(join(imagesPath,file))] # get only files
		# delete metadata
		deleteMetadataResults = pyDeleteFilesMetadata(imagesPath,allFilesName) # save when file metadata was deleted correctly
elif optionMetadata == 2:
	imagePath = raw_input('Complete route of the folder with the image (/../../..):\n>>> ')
	imageName = raw_input('Complete name of the image:\n>>> ')
	if pyCheckFileORFolderExists(imagePath,imageName,'file') == -1:
		print "ERROR: image doesn't exists"
		continueDeletingMetadata == -1
	else:
		continueDeletingMetadata = pyDeleteFileMetadata(imagePath, imageName)
		if continueDeletingMetadata == 1:
			deleteMetadataResults = pyConvert2List(continueDeletingMetadata)
			allFilesName.append(imageName)
			imagesPath = imagePath
if 1 not in deleteMetadataResults: # no file has been changed
	print 'No file has been changed'
	continueDeletingMetadata = -1
if continueDeletingMetadata != -1:
	moveORdeleteOriginalFiles(imagesPath,allFilesName,deleteMetadataResults)
print 'Process completed'