class Duck:
    def quack(self):
        print("Quaaaaaack!")

class Person:
    def quack(self):
        print("The person imitates a duck.")


if __name__ == "__main__":
    d = Duck()
    p = Person()
    list_of_objects = [d, p]
    for o in list_of_objects:
        o.quack()
