class SuperDuperBurger(object): 
    def __init__(self):
        self.components = ["potates", "chiken", "onion", "souces", "beef"]

    def __iter__(self):
        return SuperDuperIterator(self)

class SuperDuperIterator(object):
    def __init__(self, burger):
        self.burger = burger
        self.pos = 0

    def __iter__(self):
        return self

    def next(self):
        if self.pos >= len(self.burger.components):
            raise StopIteration
        next_component = self.burger.components[self.pos]
        self.pos += 1
        return next_component

if __name__ == "__main__":
    sb = SuperDuperBurger()
    for c in sb:
        print(c)
