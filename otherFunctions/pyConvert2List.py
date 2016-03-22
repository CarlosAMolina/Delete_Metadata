#!/usr/bin/python

def pyConvert2List(element):
	# if element is not a list convert to one
	# input: string, int
	if type(element)==str:
		element = element.split()
	if type(element)==int:
		int2list=[]
		int2list.append(element)
		element = int2list
	return element