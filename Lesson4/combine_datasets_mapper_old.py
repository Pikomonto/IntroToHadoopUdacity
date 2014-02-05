#!/bin/bash

# Your task is to write a mapper code that combines 2 datasets
# This is fairly involved task.
# You want to combine the datasets by joining them by the userid
# so, the mapper key should be "user_ptr_id" from "forum_users.tsv"
# and "author_id" from "forum_nodes.tsv" file. The value would be the full line
# from the respective files: either reputation and badges for the user,
# or full information about forum node.
# To be able to combine the records in the reducer you also need to know
# from which of the tables the informations comes from.
# So, the mapper should output A or B (or something similar) in front
# of the value. Output would be:
# 12345\tA"11"\t"0"\t"0"\t"0"
# 12345\tB"6336"\t"Unit 1: Same Value Q"\t"cs101 value same"  (etc...) 

# The reducer will get the values sorted, so the line starting with "A"
# will be information about the user, values starting with "B" will be forum nodes.
# Then you can store the user information, append this information to each forum node
# that this user had made, and print it out.

import sys
import csv

def mapper():

	# sets the reader for the TSV data file
    reader = csv.reader(sys.stdin, delimiter='\t',  quotechar='"', quoting=csv.QUOTE_ALL)

	# sets the writer for outputting the data to the reducer
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	# reads from TSV, record by record
    for line in reader:
        
        # if it's the users file (the TSV of users has exactly 5 fields)
        if len(line) == 5:
			
			# gets every field
            id, reputation, gold, silver, bronze = line
			
			# if is not the header of TSV
            if id.isdigit():
				
				# composes the user data in a row with the user_id as the first field,
				# prepends an 'A' character to the reputation and then add the other fields
	            row = [id,"A" + reputation, gold, silver, bronze]

				# writes the row to the reducer
	            writer.writerow(row)

        # if it's the node file (the TSV of users has exactly 19 fields)
        elif len(line) == 19:
			
			# composes the node data in a row with the user_id as the first field,
			# prepends a 'B' character to the node id, adds the title and tagnames
			# sets the key as the first field and             
			row = [line[3],"B" + line[0], line[1], line[2]]
			
			# and loops over the other field to append them to the row
			for i in range(4,19):
				row.append(line[i])

			# if it's not the header of the TSV
			if line[3].isdigit():

				# writes the row to the reducer
				writer.writerow(row)
        
# This function allows you to test the mapper with the provided test string
def main():
    #import StringIO
    #sys.stdin = StringIO.StringIO(test_text)
    mapper()
    #sys.stdin = sys.__stdin__

main()
