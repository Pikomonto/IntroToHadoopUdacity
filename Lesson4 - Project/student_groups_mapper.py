#!/usr/bin/python

import sys
import csv

nodes = {}

# use CSV reader for reading the TSV
reader = csv.reader(sys.stdin, delimiter='\t')

# skip the header 
next(reader, None)

for line in reader:
	# if the row has 19 fields
    if len(line) == 19:

        # get the type of node
        id = line[0]
        abs_parent_id = line[7]
        student_id=line[3]
        type = line[5]

        if type == 'question':
		    if not nodes.has_key(id):
		        nodes[id] = {}
		        nodes[id] = [student_id]
		    else:
				nodes[id].append(student_id)
        else:
		    if not nodes.has_key(abs_parent_id):
		        nodes[abs_parent_id] = {}
		        nodes[abs_parent_id] = [student_id]
		    else:
				nodes[abs_parent_id].append(student_id)
			

for id in nodes:
    print "{0}\t{1}".format(id,str(nodes[id]))

