#!/usr/bin/python
import sys
import csv

# To run this code on the actual data, please download the additional dataset.
# You can find instructions in the course materials (wiki) and in instructor comments.
# There are some things in this data file that are different from what you saw
# in Lesson 3. This dataset is more complicated, and closer to what you
# would see in the real world. It was generated by exporting data from
# a SQL database.
# Since the data in at least one of the fields (the body field) can include new lines,
# and all the fields are enclosed in double quotes,
# you should use a less naive way of processing the data file (instead of split(",")).
# We have provided sample code on how to use the csv module of Python.
# "line" in this case will be an array that contains all the fields
# similar to using split in the previous lesson.
###########################################################################
# In this exercise you are interested in the field "body" which is the 5th field.
# Find forum nodes where "body" contains only one sentence.
# We define sentence as a "body" that contains either none of the following
# 3 punctuation marks ".!?" , or only one of them as the last character in the body.
# You should not parse the HTML inside body, or pay attention to new lines.


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        
        # YOUR CODE HERE
        count = 0
        count += line[4].count(".")
        count += line[4].count("!")
        count += line[4].count("?")
        if line[4][len(line[4])-1] not in ["!","?","."]:
            count += 1
        #print "[" + line[4] + "]: " + str(count)
        if count <= 1:
            writer.writerow(line)



test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Also one sentence!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo sentences!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two Sentences\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one sentence\n\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
