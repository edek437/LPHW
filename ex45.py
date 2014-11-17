##Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

    def voice(self):
        print "No voice"

##Dog is-a Animal
class Dog(Animal):
    
    def __init__(self,name):
        ##name is-a Dog
        self.name=name

    def voice(self):
        print "Hau Hau"

##Cat is-a Animal
class Cat(Animal):

    def __init__(self,name):
        ##name is-a Cat
        self.name=name


##Person is-a object
class Person(object):
    
    def __init__(self,name):
        ##name is-a Person
        self.name=name

        ##Person has-a some kind of pet
        self.pet=None

##Employee is-a Person
class Employee(Person):
    def __init__(self,name,salary):
        ##name is-a Employee. what is this strange magic?
        super(Employee,self).__init__(name)
        ##Employee has-a salary
        self.salary=salary

##Fish is-a object
class Fish(object):
    pass

##Salmon is-a Fish
class Salmon(Fish):
    pass

##Halibut is-a Fish
class Halibut(Fish):
    pass


##rover is-a Dog
rover = Dog("Rover")
print "DOG:", rover.voice()

##satan is-a Cat
satan = Cat("Satan")
print "CAT:", satan.voice()

##Mary is-a Person
mary=Person("Mary")

##Mary has-a satan
mary.pet=satan

##frank is-a Employee
frank = Employee("Frank",120000)

##Frank has-a pet
frank.pet=rover

##flipper is-a Fish
flipper=Fish()

##crouse is-a Salmon
crouse=Salmon()

##harry is-a Halibut
harry=Halibut()


