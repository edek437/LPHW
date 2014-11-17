#bear_with_sword class

class BearWithSword(object):
    
    def __init__(self):
        self.next_room=None

    def room(self):
        print """Puzzled, you are about to pick up the fish poop diamond when \na bear bearing a load bearing sword walks in. \n"Hey! That's my diamond! Where'd you get that!? \nIt holds its paw out and looks at you."""

        give_it = raw_input("> ")
        if give_it=="give_it":
            print """The bear swipes at your hand to grab the diamond and \nrips your hands off in the process. IT then looks at \nyour bloody stump and says, "Oh crap, sorry about that." \nIt tries to put your hand back on, but you colapse. \nThe last thing you see id the bear shrug and eat you."""
            self.next_room='death'

        elif give_it == "say no":
            print """The bear looks shocked. Nobody ever told a bear \nwith a broadsword "no". It asks, \n"Is it because it's not a katana? I could go get one!" \nIt then runs off and now you noticw a big iron gate. \n"Where the hell did that come from?" You say.\""""
            self.next_room='big_iron_gate'
        else:
            print "The bear look puzzled as to why you'd do that."
            self.next_room='bear_with_sword'

    def go_to_next_room(self):
        return self.next_room
