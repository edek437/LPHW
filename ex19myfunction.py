def my_function(arg1, arg2):
    print "This function is adding and substracting  two given arguments %d and %d" % (arg1,arg2)
    print "Addiction: %d" % (arg1+arg2)
    print "Substraction: %d" % (arg1-arg2)


number1=30
number2=40

my_function(1,-1)
my_function(number1 - number2, 5)
my_function(-number1,-number2)
my_function(2*number2%5, number2/6)
my_function(abs(-3), max(4,number1))

