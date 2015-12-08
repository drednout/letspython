x = 1

def f():
    x = 2
    print("in f, x={}".format(x))

f()
print("globally, x={}".format(x))
