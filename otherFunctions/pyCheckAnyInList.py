#!/usr/bin/python

from pyConvert2List import pyConvert2List

def pyCheckAnyInList(list2study, list2search):
	# input
	# list2study: list of elements
	# strList2search: chek if any element is in list2study. It it is not a list, the method do the convertion
	list2search = pyConvert2List(list2search)
	for element in list2search:
		if (element in list2study) == True:
			return 1
	return -1