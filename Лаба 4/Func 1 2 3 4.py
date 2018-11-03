print("""
        ===================================================================
                              ЛАБОРАТНОРНА РОБОТА №4
                     ПРОГРАМУВАННЯ З ВИКОРИСТАННЯМ ФУНКЦІЙ
                             (ОБЧИСЛЕННЯ І ЛОГІКА)
                     АВТОР: КАСІЧ БОГДАН, КМ-83 (6 ВАРІАНТ)    
        ===================================================================
Добрий день! Дана програма дозволить вам ввести два дійсних числа , а потім
ви зможете дізнатися їх суму,різнию,добуток і частку ввівши 1,2,3 або 4 відповідно.
Програма написана за допомогою функції ariphmetic(x,y,plus,minus,multiply,divide)
                                                                                 """)

import re

def ariphmetic(x,y,plus,minus,multiply,divide):
    if plus=="1":
        return x+y
    elif minus=="2":
        return x-y
    elif multiply=="3":
        return x*y
    else:
        divide=input("print '1' if u want to  x/y \nprint '2' if u want to y/x: ")
        while divide!="1" and divide!="2":
            divide=input("Please print correct data: ")
        if divide=="1":
            try:
                return x/y
            except ZeroDivisionError:
                return "Zero cannot be divided. Please don't do that"
        else:
            try:
                return y/x
            except ZeroDivisionError:
                return "Zero cannot be divided. Please don't do that"


pattern_int = r"^[-\d]\d*$" 
pattern_float = r"^[-\d]\d*\.\d*$"
def valid_x():
    global a
    a=''
    print("Design your float x")
    while (not re.match(pattern_float,a) and not re.match(pattern_int,a)):
        a = input("Please print correct data:  ")
    return float(a)
    
def valid_y():
    global b
    b=''
    print("Design your float y")
    while (not re.match(pattern_float,b) and not re.match(pattern_int,b)):
        
        b = input("Please print correct data:  ")
    return float(b)

def valid_d():
    global d
    d=''
    print("print '1' if u want to add numbers \nprint '2' if u want to substract numbers \nprint '3' if u want to multiply numbers \nprint '4' if u want to divide numbers")
    while (d!="1" and d!="2" and d!="3" and d!="4"):
        d = input("Please print correct data: ")
    if d=="1":
        return "Sum x+y"
    elif d=="2":
        return "Difference x-y"
    elif d=="3":
        return "Product x*y"
    else:
        return "Quotient"

print(valid_x())
print(valid_y())
print(valid_d())
print(ariphmetic(float(a),float(b),d,d,d,d))


answer=input("print 'stop' if u want to stop the prog:  ")
while answer!="stop":
    switch=input("print 'switch' if u want to swtich the number: ")
    if switch=="switch":
        print(valid_x())
        print(valid_y())
        print(valid_d())
        print(ariphmetic(float(a),float(b),d,d,d,d))
        answer=input("print 'stop' if u want to stop the prog:  ")
        continue
    else:
         print(valid_d())
         print(ariphmetic(float(a),float(b),d,d,d,d))
         answer=input("print 'stop' if u want to stop the prog:  ")
         continue
    
