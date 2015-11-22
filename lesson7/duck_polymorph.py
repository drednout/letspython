from duck_inheritance import Duck, SpeechlessDuck

class FlyingDuck(Duck):
    def fly(self):
        print("{} is flying".format(self.name))

if __name__ == "__main__":
    duck_list = [
        Duck("McDuck"), 
        SpeechlessDuck("SpeechlessDuck"),
        FlyingDuck("Zigzag McDuck"),
    ]
    for duck in duck_list:
        duck.say("hello")
    print("What about flying?")
    for duck in duck_list:
        duck.fly()
