import re

def coefs():
    global n
    cfs = []
    try:
        n = int(input("Enter the order of your polynomial: "))
    except ValueError:
        print("Enter the correct data")
        return coefs()
    if n < 0 or n >50 :
        print("Enter the correct data")
        return coefs()
    i = n
    while len(cfs) <= n:
        print("Enter the coefficient to the corresponding item with the power of: ", i)
        j = input()
        while not re.match(pattern_float, j) and not re.match(pattern_int, j):
            print("Enter valid numbers only, please")
            print("Enter the coefficient to the corresponding item with the power of: ", i)
            j = input()
        cfs.append(float(j))
        i = i - 1
    cfs.reverse()
    return cfs

def dx(f, x):
    return abs(f(x, g, w))


def newtons_method(f, df, x0, e):
    iters = 0
    delta = dx(f, x0)
    while delta > e:
        try:
            x0 = x0 - f(x0, g, w) / df(x0)
        except ZeroDivisionError:
            return
        iters = iters + 1
        if iters > 100:
            return
        else:
            delta = dx(f, x0)
    x0 = round(x0, 3)
    return x0


def df(x):
    h = 1e-5
    return round((f(x + h, g, w) - f(x - h, g, w)) / (2 * h))


def f(x, g, w):
    if g <= n:
        return w[0] + f(x, g + 1, w[1:]) * x
    if g > n:
        return 0

def real():
    global g,w
    g = 0
    w = coefs()
    a = set()
    for x0 in range(-1000000, 1000000, 100000):
        c = newtons_method(f, df, x0, 1e-5)
        a.add(c)
    for x0 in range(-100000, 100000, 10000):
        c = newtons_method(f, df, x0, 1e-5)
        a.add(c)
    for x0 in range(-10000, 10000, 1000):
        c = newtons_method(f, df, x0, 1e-5)
        a.add(c)
    for x0 in range(-1000, 1000, 100):
        c = newtons_method(f, df, x0, 1e-5)
        a.add(c)
    for x0 in range(-100, 100, 10):
        c = newtons_method(f, df, x0, 1e-5)
        a.add(c)
    for x0 in range(-10, 10, 1):
        c = newtons_method(f, df, x0, 1e-5)
        a.add(c)
    for x0 in less_than_abs_one:
        c = newtons_method(f, df, x0, 1e-5)
        a.add(c)
    if (len(a) == 1 and None in a) or (len(a) == 0):
        print("No roots")
    else:
        if len(a) < 100:
            for i in a:
                if i != None:
                    print("x=", i)
        else:
            print("Infinite number of roots")


pattern_int = r"^[-\d]?\d+$"
pattern_float = r"^[-\d]\d*\.\d*$"
less_than_abs_one=[-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
real()
answer = input("Type 'stop' if u want to stop the prog: ")
while answer != 'stop':
    real()
    answer = input("Type 'stop' if u want to stop the prog: ")
