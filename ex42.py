#another game with rooms and a lot of prints in class

from sys import exit
from random import randint


class Game(object):
    def __init__(self,start):
        self.quips = ["You died. You kinda suck at this.",
                 "Your mom would be proud. If she were smarter.",
                 "Such a loser.",
                 "I have a small puppy that's better at this."]
        self.start=start

    def death(self):
        print self.quips[randint(0,len(self.quips)-1)]
        exit(1)

    def princess_lives_here(self):
        print "You see a beatiful Princess with a shiny crown. \nShe offers you some cake."

        eat_it = raw_input("> ")

        if eat_it == "eat it":
            print "You explode like pinata full of frogs. \nThe Princess cackles and eats the frogs. Yum!"
            return 'death'

        elif eat_it == "do not eat it" or eat_it=="no":
            print "She throw the cake at you and it cuts off your head. \nThe last thing you see is her munching on your torso. Yum!"
            return 'death'

        elif eat_it == "make her eat it":
            print """The princess scream as you cram the cake in her mouth.
    Then she smiles and cries and thanks you for saving her.
    She pointsto a tiny door and says, 'The Koi needs cake too.'
    She gives you the very last bit of cake and shoves you in."""
            return 'gold_koi_pond'

        elif eat_it == 'cake is a lie':
            print "You make Princess laugh. She throw away poison cake and marry you. But she was a bitch so you killed her and take all gold for youlsefl. Congratulation!!! You win!!!"
            exit(1)

        else:
             print "The Princess looks at you confused and just points at the cake."
             return 'princess_lives_here'

    def gold_koi_pond(self):
        print """There is a garden with a koi pond in the center. \nYou walk close and see a massive fin poke out. \nYou peek in and a creepy looking huge Koi stares at you. \nIt opens its mouth waiting for food."""

        feed_it = raw_input("> ")

        if feed_it == "feed it":
            print """The Koi jumps up, and rather than eating the cake, eats your arm. \nYou fall in and the Koi shrugs than eats you. \nYou are then poped out sometime later."""
            return 'death'

        elif feed_it == "do not feed it" or feed_it == 'no':
            print """The koi grimaces, then thrashes around for a second. \nIt rushes to the other end of the pond, braces against the wall... \nthen it *lunges* out of water, up in the air and over your \n entire body, cake and all. \nYou are then pooped out a week later."""
            return 'death'

        elif feed_it == "throw it in" or feed_it == "throw":
            print """The koi wiggles, then leaps into the air to eat the cake. \nYou can see it's happy, it then grunts, trashes... \nand finally rolls over and poops a magic diamond into the air \nat your feet."""
            return 'bear_with_sword'

        else:
            print "The Koi gets annoyed and wiggles a bit."
            return 'gold_koi_pond'

    def bear_with_sword(self):
        print """Puzzled, you are about to pick up the fish poop diamond when \na bear bearing a load bearing sword walks in. \n"Hey! That's my diamond! Where'd you get that!? \nIt holds its paw out and looks at you."""

        give_it = raw_input("> ")
        if give_it=="give_it":
            print """The bear swipes at your hand to grab the diamond and \nrips your hands off in the process. IT then looks at \nyour bloody stump and says, "Oh crap, sorry about that." \nIt tries to put your hand back on, but you colapse. \nThe last thing you see id the bear shrug and eat you."""
            return 'death'

        elif give_it == "say no":
            print """The bear looks shocked. Nobody ever told a bear \nwith a broadsword "no". It asks, \n"Is it because it's not a katana? I could go get one!" \nIt then runs off and now you noticw a big iron gate. \n"Where the hell did that come from?" You say.\""""
            return 'big_iron_gate'
        else:
            print "The bear look puzzled as to why you'd do that."
            return 'bear_with_sword'

    def big_iron_gate(self):
        print "You walk up to the big iron gate and see there's a handle."
        open_it = raw_input("> ")

        if open_it == 'open_it':
            print""" You open it and you are free! \nThere are mountains. And berries! And... you forgot about bear who has just came back and is now stabing you with his katana. \n"Who's laughing now!? Love this katana\""""
            return 'death'
        else:
            print "Door + handle, What are you waiting for?"
            return 'big_iron_gate'

    def play(self):
        next = self.start
        while True:
            room=getattr(self,next)
            next = room()

a_game=Game("princess_lives_here")
a_game.play()
    
