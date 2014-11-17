#Printing marathin phase 2
formater = "%r %r %r %r"

print formater % (1,2,3,4)
print formater % ('one','two','three','four')
print formater % (True, False, False, True)
print formater % (formater, formater, formater, formater)
print formater % ("string", 3 , False , formater)
print formater % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.", #this will be printed in double quotes because it has single quote inside
        "So I said goodnight."
)
