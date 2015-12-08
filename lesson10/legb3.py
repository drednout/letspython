x = 1

def f():
    global x
    x = 2
    print("in f, x={}".format(x))

f()
print("globally, x={}".format(x))
