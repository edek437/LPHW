#Names, Variables, Code, Functions

#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1,arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

#this just takes one argument
def print_one(arg1):
    print "arg1: %r" %arg1

#this one takes no arguments
def print_none():
    print "I got nothing"

#fun checklist for further execises
def checklist(*args):
    arg1, arg2, arg3 =args
    print("TODO: %r, %r, %r")%(arg1,arg2,arg3)

print_two('edek','437')
print_two_again('edek','437')
print_one('edek_437')
print_none()
checklist('nothing','vacuum room', 'wash dishes')
