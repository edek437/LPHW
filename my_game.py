#my game
from sys import exit

class Human(object):
    def __init__(self):
        self.blue_card=False
        self.red_card=False
        self.yellow_card_no1=False
        self.yellow_card_no2=False
        self.green_card=False
        self.purple_card=False
        self.steps=100
    def show_steps_remaining(self):
        return self.steps
    def show_inventory(self):
        print "blue card : %r \nred card: %r \nyellow card 1: %r \nyellow card 2: %r \ngreen card: %r \npurple card: %r"%(self.blue_card, self.red_card, self.yellow_card_no1, self.yellow_card_no2, self.green_card, self.purple_card)

def check_if_room_accesible(hero, floor, room_no):
    if (floor==1 and room_no==1 and  hero.blue_card==False):
        print "You need blue card to pass"
        return False
    elif(floor==2 and room_no==0 and  hero.red_card==False):
        print "You need red card to pass"
        return False
    elif(floor==4 and room_no==9 and  (hero.yellow_card_no1==False or hero.yellow_card_no2==False)):
        print "You need yellow cardS! to pass"
        return False
    elif(floor==3 and room_no==6 and  hero.green_card==False):
        print "You need green card to pass"
        return False
    elif(floor==4 and room_no==10 and  hero.purple_card==False):
        print "You need purple card to pass"
        return False
    else:
        return True

def card_found(hero, floor, room_no):
    if (floor==3 and room_no==2):
        print "You found blue card. Check your inventory"
        hero.blue_card=True
        return
    elif (floor==4 and room_no==14):
        print "You found red card. Check your inventory"
        hero.red_card=True
        return
    elif (floor==4 and room_no==2):
        print "You found yellow card no1. Check your inventory"
        hero.yellow_card_no1=True
        return
    elif (floor==4 and room_no==5):
        print "You found yellow card no2. Check your inventory"
        hero.yellow_card_no2=True
        return
    elif (floor==4 and room_no==9):
        print "You found green card. Check your inventory"
        hero.green_card=True
        return
    elif (floor==4 and room_no==13):
        print "You found purple card. Check your inventory"
        hero.purple_card=True
        return    
    else:
        return

def left_or_right(next,floor,room_no,hero):
    if next == "right":
        hero.steps-=1
        next_room(hero,floor+1,2*room_no+1)
    elif next == "left":
        hero.steps-=1
        next_room(hero,floor+1,2*room_no)
    elif next == "inv" :
        hero.show_inventory()
    else:
        return

def win(floor,room_no):
    if floor==4 and room_no==10:
        print "Congratulation!! You have just obtained Permit 38A"
        exit(0)
    else:
        return

def next_room(hero,floor,room_no):
    print "You have %d steps left" % hero.show_steps_remaining()
    print "You are in room %d on floor %d" %(room_no,floor)
    if not check_if_room_accesible(hero, floor, room_no):
        hero.steps-=floor
        start(hero)
    card_found(hero, floor, room_no)
    win(floor,room_no)
    if floor==4:
        hero.steps+=2
        print("You came to highest floor. Go back to start.")
        start(hero)
    while True:
        print "You have %d steps left" % hero.show_steps_remaining()
        print "Go right, left or return to start? (check inventory = inv)"
        next = raw_input("> ")
        if next == "start":
            hero.steps-=floor
            start(hero)
        else:
            left_or_right(next,floor,room_no,hero)

def start(hero):
    floor=0
    room_no=0
    print "You are in room %d on floor %d" %(0,0)
    while True:
        print "You have %d steps left" % hero.show_steps_remaining()
        print "Go right or left? (check inventory = inv)"
        next = raw_input("> ")
        left_or_right(next,floor,room_no,hero)


print """
Have you watched the 12 tasks of Asterix? If yes you should remember the task with obtaining the Permit 38A. This is your task now. If not watch it. Now I'll explain game in details. You have 100 steps to find "Permit 38A". You beggin in starting point and can move left (type'left'), right (type 'right) or go back to start (type 'start'). Aftergetting to 1 of 16 end points you return to start point and 2steps are added. You lose one step per decision. Some point arerestricted if you don't posses card in given color. So you need to find these before finally getting to point where Permit 38A is. Good luck!! Khihihihihi!!!
"""
hero=Human()
start(hero)
