#more files
from sys import argv
from os.path import exists
from os import close

script, from_file, to_file = argv

#print "Copying from %s to %s" %(from_file,to_file)

#we could do these in one line
#input=open(from_file)
#indata=input.read()
#indata=open(from_file).read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#output = open(to_file,'w')
#output.write(indata)
#open(to_file,'w').write(indata)

#print "allrigth, all done"

#output.close()
#input.close()

#ex17 w 1 linijce
open(to_file,'w').write(open(from_file).read())
