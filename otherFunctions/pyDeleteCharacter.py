#!/usr/bin/python

from pyConvert2List import pyConvert2List

def pyDeleteCharacter(list2change, character2delete):

	# replate in all the elements of a list	
	# use:
	# from pyDeleteCharacter import pyDeleteCharacter; pyDeleteCharacter('holaM','M')
	# variables:
	# output:list
	
	if type(character2delete) == str:

		# if list2change is not a list convert to one
		list2change = pyConvert2List(list2change)

		# delete at each element
		for index, element in enumerate(list2change):
			if character2delete in element:
				list2change[index] = element.replace(character2delete, "")

		return list2change

	else:
		print 'ERROR pyDeleteCharacter: introduce a character to delete'
		return -1
