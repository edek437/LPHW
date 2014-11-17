#More variables and names

nickname = 'edek437'
age = 22
height = 183.5 #cms
weight = 70.5 #kg
eyes = 'brown'
teeth = 'yellow'
hair = 'brown'

print "Let's talk about %s." % nickname
print "He's %f cms tall what is equal to %f inches" % (height,height*0.39)
print "He's %f kilos heavy whis is equal to %f pounds" % (weight, 2.2*weight)
print "Actually that's not heavy"
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print " If I add %d, %f, and %f I get %f." %(age,height,weight,age+height+weight)
