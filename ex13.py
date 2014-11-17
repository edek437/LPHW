# Parameters, Unpacking, Variables

#sys is the module(library)
from sys import argv

#unpacking argv to variables
script, first, second =argv
third=raw_input("Enter 3rd argument: ")

print "The script is called: ", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

