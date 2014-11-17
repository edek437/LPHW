# princess_lives_here class

class PrincessLivesHere(object):
    def __init__(self):
        self.next_room=None

    def room(self):
        print "You see a beatiful Princess with a shiny crown. \nShe offers you some cake."

        eat_it = raw_input("> ")

        if eat_it == "eat it":
            print "You explode like pinata full of frogs. \nThe Princess cackles and eats the frogs. Yum!"
            self.next_room='death'

        elif eat_it == "do not eat it" or eat_it=="no":
            print "She throw the cake at you and it cuts off your head. \nThe last thing you see is her munching on your torso. Yum!"
            self.next_room='death'

        elif eat_it == "make her eat it":
            print """The princess scream as you cram the cake in her mouth.
    Then she smiles and cries and thanks you for saving her.
    She pointsto a tiny door and says, 'The Koi needs cake too.'
    She gives you the very last bit of cake and shoves you in."""
            self.next_room='gold_koi_pond'

        elif eat_it == 'cake is a lie':
            print "You make Princess laugh. She threw away poison cake and married you. But she was a bitch so you killed her and took entire gold for yourself. Congratulation!!! You win!!!"
            exit(1)

        else:
             print "The Princess looks at you confused and just points at the cake."
             self.next_room='princess_lives_here'

    def go_to_next_room(self):
        return self.next_room

