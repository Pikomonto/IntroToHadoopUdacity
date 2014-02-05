#!/usr/bin/python

import sys
import csv

users = {}

# use CSV reader for reading the TSV
reader = csv.reader(sys.stdin, delimiter='\t')

# skip the header 
next(reader, None)

for line in reader:
	# if the row has 19 fields and the "added_at" field is longer than 13 chars
    if len(line) == 19 and len(line[8]) > 13:

		# get the ID and the hour (we're confident the the hour 
		# will be always at position 11 and 12 of the string)
        id = line[3]
        hour = line[8][11:13]

		# if ID and hour are numbers
        if hour.isdigit() and id.isdigit():

			# if it's the first time we see this user, we create a new dictionary
            if not users.has_key(id):
                users[id] = {}
			
			# if it's not the first time this user writes a post at this hour, 
			# we increment the number of post for this hour
            if users[id].has_key(hour):
                users[id][hour] += 1

			# if it's the first time, we set to 1 the number of post at this hour
            else:
                users[id][hour] = 1    
                    
# we output to the reducers the id of the user and the dictionary of the number of posts
for user in users:
    print "{0}\t{1}".format(user,users[user])
