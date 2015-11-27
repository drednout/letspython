def get_components(burger):
    for component in burger.components:
        yield component

class SuperDuperBurger(object): 
    def __init__(self):
        self.components = ["potates", "chiken", "onion", "souces", "beef"]

    def __iter__(self):
        return get_components(self)


if __name__ == "__main__":
    sb = SuperDuperBurger()
    for c in sb:
        print(c)
