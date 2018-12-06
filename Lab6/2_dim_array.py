print("""
        ===================================================================
                               ЛАБОРАТНОРНА РОБОТА №6
                             РЕКУРСІЯ ТА ОБРОБКА МАТРИЦЬ
                        Завдання на двовимірні масиви (матриці)
                        АВТОР: КАСІЧ БОГДАН, КМ-83 (6 ВАРІАНТ)    
        ===================================================================
Добрий день! Дана програма дозволить вам створити матрицю дійсних чисел поелементно.
А потім вона виведе суму усіх елементів матриці, саму матрицю з додатковим рядком, в якому 
знаходятся числа які визначають частку суми елементів стовця в основній сумі елементів матриці.
                                                                                 """)
from re import match
pattern_int = r"^[-\d]\d*$"
pattern_float = r"^[-\d]\d*\.\d*$"

def columns():
    m = input("Number of columns: ")
    while not match(pattern_int, m):
        m = input("Type integer only please:  ")
    m = int(m)
    while m <= 0:
        m = input("Type integer higher than zero please:  ")
        while not match(pattern_int, m):
            m = input("Type integer only please: ")
        m=int(m)
    return int(m)

def rows():
    n = input("Number of rows: ")
    while not match(pattern_int, n):
        n = input("Type integer only please:  ")
    n = int(n)
    while n <= 0:
        n = input("Type integer higher than zero please:  ")
        while not match(pattern_int, n):
            n = input("Type integer only please: ")
        n=int(n)
    return int(n)

def elems(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            message = "Print your float number to a[" + str(j) + "][" + str(i) + "]: "
            a[i][j] = input(message)
            while not match(pattern_int,a[i][j]) and not match(pattern_float,a[i][j]):
                print("Print correct data")
                a[i][j]=input(message)
            a[i][j] = float(a[i][j])
    return a

m=columns()
n=rows()
a = [[0] * n for i in range(m)]
elems(a)
s=0
for i in range(len(a)):
    temp=sum(a[i])
    s+=temp
    a[i].append(temp)
if s!=0:
    print()
    print("Sum of all elements="+str(s))
    print()
else:
    print()
    print("Sum of all elements equal to zero \nso we cannot find the quotient values in the columns")
for i in range(len(a)):
    try:
        a[i][-1]=round(a[i][-1]/s,3)
    except ZeroDivisionError:
        print()
for j in range(n + 1):
    for i in range(m):
        print(a[i][j], end=" ")
    print()

answer=input("print 'stop' if u want to stop the prog:  ")
while answer!="stop":
    m = columns()
    n = rows()
    a = [[0] * n for i in range(m)]
    elems(a)
    s = 0
    for i in range(len(a)):
        temp = sum(a[i])
        s += temp
        a[i].append(temp)
    if s != 0:
        print()
        print("Sum of all elements=" + str(s))
        print()
    else:
        print()
        print("Sum of all elements equal to zero \nso we cannot find the quotient values in the columns")
    for i in range(len(a)):
        try:
            a[i][-1] = round(a[i][-1] / s, 3)
        except ZeroDivisionError:
            print()
    for j in range(n + 1):
        for i in range(m):
            print(a[i][j], end=" ")
        print()
    answer = input("print 'stop' if u want to stop the prog:  ")

