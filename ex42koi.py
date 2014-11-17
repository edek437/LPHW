#gold_koi_pond class

class GoldKoiPond(object):
    def __init__(self):
        self.next_room=None

    def room(self):
        print """There is a garden with a koi pond in the center. \nYou walk close and see a massive fin poke out. \nYou peek in and a creepy looking huge Koi stares at you. \nIt opens its mouth waiting for food."""

        feed_it = raw_input("> ")

        if feed_it == "feed it":
            print """The Koi jumps up, and rather than eating the cake, eats your arm. \nYou fall in and the Koi shrugs than eats you. \nYou are then poped out sometime later."""
            self.next_room='death'

        elif feed_it == "do not feed it" or feed_it == 'no':
            print """The koi grimaces, then thrashes around for a second. \nIt rushes to the other end of the pond, braces against the wall... \nthen it *lunges* out of water, up in the air and over your \n entire body, cake and all. \nYou are then pooped out a week later."""
            self.next_room='death'

        elif feed_it == "throw it in" or feed_it == "throw":
            print """The koi wiggles, then leaps into the air to eat the cake. \nYou can see it's happy, it then grunts, trashes... \nand finally rolls over and poops a magic diamond into the air \nat your feet."""
            self.next_room='bear_with_sword'

        else:
            print "The Koi gets annoyed and wiggles a bit."
            self.next_room='gold_koi_pond'

    def go_to_next_room(self):
        return self.next_room
