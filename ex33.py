#While loops

def while_loop(while_condition, increment):
    i = 0
    numbers = []
    for i in range(0,while_condition,increment):
 #   while i<while_condition:
        print "At the top i is %d" % i
        numbers.append(i)
 #       i+=increment
        print "Number now: ",numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num


while_loop(20,4)
