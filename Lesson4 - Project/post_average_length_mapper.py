#!/usr/bin/python

import sys
import csv

posts = {}

# use CSV reader for reading the TSV
reader = csv.reader(sys.stdin, delimiter='\t')

# skip the header 
next(reader, None)

for line in reader:
	# if the row has 19 fields
    if len(line) == 19:

        # get the type of node
        type = line[5]
        id = line[0]
        parent_id = line[6]
        length = int(len(line[4]))
        #print "type: " + type + "\tid: " + id + "\t\tparent: " + parent_id + "\tabs: " + abs_parent_id
        if type == 'question':
            posts[id] = {}
            posts[id]['length'] = length
        elif type == 'answer':
            if posts.has_key(parent_id):
                posts[parent_id][id] = length

for post in posts:
    tot_len = 0
    for answer in posts[post]:
        if answer != 'length':
            tot_len += posts[post][answer]
    print "{0}\t{1}".format(post,str(posts[post]['length'])+"|"+str(tot_len)+"|"+str(len(posts[post])-1))

