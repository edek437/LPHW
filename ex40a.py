#Dictionaries

cities = {'CA' : 'San Francisko', 'MI':'Detroit','FL':'Jasonville'}

cities ['NY']='New York'
cities ['DS']='Wroclaw'
cities ['OR']='Portland'
cities ['ZK']='Koszalin'
cities ['RAND']='Random'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."


#ok pay attention!
cities['_find']=find_city

for i in range(len(cities)):
    print cities.items()[i]
