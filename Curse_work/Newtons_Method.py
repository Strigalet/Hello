def coefs():
    global n
    cfs=[]
    try:
        n=int(input("Введіть порядок вашого поліному від 0 до 10: "))
    except ValueError:
        print("Введіть коректні дані")
        return coefs()
    if n>10 or n<0:
        print("Введіть коректні дані")
        return coefs()
    i=n
    while len(cfs)<=n:
        print("Введіть коефіцієнт до відповідного елементу зі степенню: ",i)
        cfs.append(float(input()))
        i=i-1
    cfs.reverse()
    return cfs

def dx(f, x):
    return abs(f(x,g,w))


def newtons_method(f, df, x0, e):
    iters=0
    delta = dx(f, x0)
    while delta > e:
        try:
            x0 = x0 - f(x0,g,w) / df(x0)
        except ZeroDivisionError:
            return
        iters=iters+1
        if iters > 100:
            return
        else:
            delta = dx(f, x0)
    x0 = round(x0, 5)
    return x0


def df(x):
    h = 1e-5
    return round((f(x+h,g,w) - f(x-h,g,w)) / (2 * h))

def f(x,g,w):
    if g<=n:
        return w[0]+f(x,g+1,w[1:])*x
    if g>n:
        return 0
g=0
w=coefs()
a = set()
for x0 in range(-1000000,1000000,100000):
    c = newtons_method(f, df, x0, 1e-5)
    a.add(c)
for x0 in range(-100000,100000,10000):
    c = newtons_method(f, df, x0, 1e-5)
    a.add(c)
for x0 in range(-10000,10000,1000):
    c = newtons_method(f, df, x0, 1e-5)
    a.add(c)
for x0 in range(-1000,1000,100):
    c = newtons_method(f, df, x0, 1e-5)
    a.add(c)
for x0 in range(-100,100,10):
    c = newtons_method(f, df, x0, 1e-5)
    a.add(c)
for x0 in range(-10,10,1):
    c = newtons_method(f, df, x0, 1e-5)
    a.add(c)
if (len(a)==1 and None in a) or (len(a) == 0):
    print("No roots")
else:
    for i in a:
        if i != None:
            print("x=", i)

