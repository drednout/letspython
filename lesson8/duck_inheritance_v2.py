class Duck(object):
    def __init__(self, name):
        self.name = name

    def say(self, msg):
        print("{} said: {}".format(self.name, msg))


class ColorfulDuck(Duck):
    def __init__(self, name, color=None):
        super(ColorfulDuck, self).__init__(name)
        #Duck.__init__(self, name)
        self.color = color

    def say(self, msg):
        # do not say anything
        print("{} with color {} said: {}".format(self.name, self.color, msg))
   

if __name__ == "__main__":
    duck1 = Duck("McDuck")
    duck2 = ColorfulDuck("ColorfulDuck1")
    duck3 = ColorfulDuck("ColorfulDuck2", color="red")
    duck1.say("Hello")
    duck2.say("Hello")
    duck3.say("Hello")
