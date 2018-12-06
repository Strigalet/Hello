print("""
        ===================================================================
                              ЛАБОРАТНОРНА РОБОТА №6
                            РЕКУРСІЯ ТА ОБРОБКА МАТРИЦЬ
                          Завдання на одновимірні масиви
                       АВТОР: КАСІЧ БОГДАН, КМ-83 (6 ВАРІАНТ)    
        ===================================================================
Добрий день! Дана програма дозволить вам ввести поелементно массив дійсних чисел,
а потім програма виведе суму всіх елементів та кількість додатніх, поставивши їх
на 0 и 1 позицію у массиві відповідно
                                                                                 """)
from re import match
import numpy as np
def get_elems():
    user_input=input("Type 'eno' if u want to stop typing. Type your float number: ")
    if user_input=="eno":
        return
    else:
        while not match(pattern_float,user_input) and not match(pattern_int,user_input):
            print("Type digits only")
            return get_elems()
    a.append(float(user_input))
    return get_elems()

def get_all_positives(a):
    counter=0
    for i in a:
        if i > 0:
            counter+=1
    return counter




a=[]
pattern_int = r"^[-\d]\d*$"
pattern_float = r"^[-\d]\d*\.\d*$"
get_elems()
sum_elems = sum(a)
all_positives=get_all_positives(a)
print("sum:",np.array([sum_elems]))
print("positives:",np.array([all_positives]))
print("your array:",np.array(a))
a.insert(0,all_positives)
a.insert(0,sum_elems)
print("resulting array:",np.array(a))
answer = input("Type 'stop' if u want to stop the prog: ")
while answer != 'stop':
    a = []
    get_elems()
    sum_elems = sum(a)
    all_positives = get_all_positives(a)
    print("sum:", np.array([sum_elems]))
    print("positives:", np.array([all_positives]))
    print("your array:", np.array(a))
    a.insert(0, all_positives)
    a.insert(0, sum_elems)
    print("resulting array:", np.array(a))
    answer = input("Type 'stop' if u want to stop the prog: ")