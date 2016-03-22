#!/usr/bin/python

import subprocess as sub
from pyDeleteCharacter import pyDeleteCharacter
from pyList2Str import pyList2Str

def pyCommandLine(command):
	# command=[command,arg1,arg2,arg3,...]
	# variables
	# input: list of strings
	# output: string

	# launch terminal order
	p=sub.Popen(command,stdout=sub.PIPE,stderr=sub.PIPE)

	# save results
	output, errors = p.communicate()

	# notify errors
	if errors != '':
		print 'ERROR ' + str(errors)
		return -1

	# delete \n
	output = pyDeleteCharacter(output,'\n')
	# list to string
	output = pyList2Str(output)

	# retrieve results
	return output