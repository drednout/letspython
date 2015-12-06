def get_components(burger):
    print("before for")
    for component in burger.components:
        print("before yield")
        yield component
        print("after yield")
    print("after for")

class SuperDuperBurger(object): 
    def __init__(self):
        self.components = ["potates", "chiken", "onion", "souces", "beef"]

    def __iter__(self):
        return get_components(self)


if __name__ == "__main__":
    sb = SuperDuperBurger()
    for c in sb:
        print(c)
