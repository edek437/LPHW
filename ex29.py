#if

people=200
cats=30
dogs=200

if (people < cats)==False:
    print "Too many cats! The world is doomed!"
if people > cats:
    print "Not many cats! The world os saved!"
if people <dogs:
    print "The world is drooled on!"
elif people==dogs:
    print "It's OK"
else:
    print "This world is dry!"

dogs+=5

if people >= dogs:
    print "People are greater than equal to dogs."
if people <= dogs:
    print "People are less than equal to dogs."
if people==dogs:
    print "people are dogs."

