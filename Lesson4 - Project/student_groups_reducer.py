#!/usr/bin/python

import sys
import ast

nodes = {}

# read from the output of mappers
for line in sys.stdin:
	
	# divides the row using the tab as splitter
    data_mapped = line.strip().split("\t")

	# if there aren't exactly two fields, there's an error
    if len(data_mapped) != 2:
        continue
	
	# get the id of the post and the list of the students posting in it
    id, str_data = data_mapped
	
	# transforms the string representation of the list
	# into a real list
    node = ast.literal_eval(str_data)
    
	# if it's the first time we see this user, we assign to it 
	# the dictionary
    if not nodes.has_key(id):
    	nodes[id] = node

	# if we already have this user
    else:

		
		# adds every student in the list got from mapper to the list here in the reducer
        for student_id in node:

			nodes[id].append(student_id)

# outputs the desired info
for id in nodes:
    print "{0}\t{1}".format(id,str(nodes[id]))

