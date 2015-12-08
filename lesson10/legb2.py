x = 1


def g():
    def f():
        print("in f, x={}".format(x))
    x = 3
    print("in g, x={}".format(x))
    f()


g()
print("globally, x={}".format(x))
