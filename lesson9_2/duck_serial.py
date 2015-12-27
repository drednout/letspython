import json

class Duck(object):
    def __init__(self, name=None):
        self.name = name

    def as_dict(self):
        d = {
            "type": self.__class__.__name__,
            "name": self.name
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.name = object_as_dict["name"]
        return object_as_dict


    def __str__(self):
        return '{}(name="{}")'.format(self.__class__.__name__, self.name)


class ColoredDuck(Duck):
    def __init__(self, name=None, color=None):
        Duck.__init__(self, name)
        self.color = color

    def as_dict(self):
        d = Duck.as_dict(self)
        d["color"] = self.color
        return d

    def load(self, file_object):
        object_as_dict = Duck.load(self, file_object)
        self.color = object_as_dict["color"]
        return object_as_dict

    def __str__(self):
        return '{}(name="{}", color="{}")'.format(self.__class__.__name__, self.name, self.color)



if __name__ == "__main__":
    duck1 = Duck("Donald Duck")
    duck1.save(open("donald_duck.txt", "w"))
    print("duck1 is {}".format(duck1))

   
    deserialized_duck = Duck()
    deserialized_duck.load(open("donald_duck.txt"))
    print("deserialized duck is {}".format(deserialized_duck))

    colored_duck = ColoredDuck(name="Colored Duck", color="red")
    colored_duck.save(open("colored_duck.txt", "w"))
    print("colored_duck is {}".format(colored_duck))

    deserialized_colored_duck = ColoredDuck()
    deserialized_colored_duck.load(open("colored_duck.txt"))
    print("deserialized colored duck is {}".format(deserialized_colored_duck))
