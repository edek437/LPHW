#game with at least 2 classes: Map and Engine (when its done :)
#now i exported each room to it's own class
from sys import exit
from random import randint
import ex42princess as prin
import ex42koi as koi
import ex42bear as bear
import ex42gate as gate

class Map(object):
    def __init__(self,start):
        self.start=start
        self.plh=prin.PrincessLivesHere()
        self.gkp=koi.GoldKoiPond()
        self.bws=bear.BearWithSword()
        self.big=gate.BigIronGate()


class Engine(object):
    def __init__(self,game_map):
        self.quips = ["You died. You kinda suck at this.",
                 "Your mom would be proud. If she were smarter.",
                 "Such a loser.",
                 "I have a small puppy that's better at this."]
        self.map=game_map


    def death(self):
        print self.quips[randint(0,len(self.quips)-1)]
        exit(1)

    def princess_lives_here(self):
        self.map.plh.room()
        return self.map.plh.go_to_next_room()

    def gold_koi_pond(self):
        self.map.gkp.room()
        return self.map.gkp.go_to_next_room()

    def bear_with_sword(self):
        self.map.bws.room()
        return self.map.bws.go_to_next_room()

    def big_iron_gate(self):
        self.map.big.room()
        return self.map.big.go_to_next_room()
        
    def play(self):
        next = self.map.start
        while True:
            room=getattr(self,next)
            next = room()

game_map=Map("princess_lives_here")
game=Engine(game_map)
game.play()
    
