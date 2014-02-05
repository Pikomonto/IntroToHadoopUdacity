#!/usr/bin/python

import csv
import sys
import re

words = {}

#reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', doublequote=True, quoting=csv.QUOTE_ALL)
reader = csv.reader(sys.stdin, delimiter='\t')
for row in reader:
	if len(row)>4:
		body = row[4]
		id = row[0]
		clean_body = re.sub('[,.<>/!?:;"()\[\]#\$=-]', ' ', body)
		row_words = clean_body.split(' ')
		if len(row_words) > 0:
			for word in row_words:
				if word == ' ':
					continue
				word = word.strip().lower()
				if words.has_key(word):
					words[word] += id + ","
				else:
					words[word] = id + ","

for word in words:
	print "{0}\t{1}".format(word,words[word][:len(words[word])-1])

