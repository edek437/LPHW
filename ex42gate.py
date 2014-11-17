#big_iron_gate class

class BigIronGate(object):

    def __init__(self):
        self.next_room=None

    def room(self):
        print "You walk up to the big iron gate and see there's a handle."
        open_it = raw_input("> ")

        if open_it == 'open it':
            print""" You open it and you are free! \nThere are mountains. And berries! And... you forgot about bear who has just came back and is now stabing you with his katana. \n"Who's laughing now!? Love this katana\""""
            self.next_room='death'
        else:
            print "Door + handle, What are you waiting for?"
            self.next_room='big_iron_gate'

    def go_to_next_room(self):
        return self.next_room
