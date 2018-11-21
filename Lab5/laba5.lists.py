print("""
        ===================================================================
                              ЛАБОРАТНОРНА РОБОТА №5
                    СТРУКТУРИ ДАНИХ: СПИСКИ,КОРТЕЖИ, МНОЖИНИ
                             (РОБОТА ІЗ СПИСКАМИ)
                     АВТОР: КАСІЧ БОГДАН, КМ-83 (6 ВАРІАНТ)    
        ===================================================================
Добрий день! Дана програма дозволить вам через пробіл ввести два списки цілих чисел,
а потім вам виведеться перетин усіх їхніх елементів, включаючи повтори
                                                                                 """)


def common_elems(a,b):
    if len(a)==0 or len(b)==0:
        return common
    if a[0]==b[0]:
        common.append(a[0])
        return common_elems(a[1:],b[1:])
    if a[0]!=b[0] and a[0]<b[0]:
        return common_elems(a[1:],b)
    if a[0]!=b[0] and a[0]>b[0]:
        return common_elems(a,b[1:])


def get_list(a):
    print("Введіть свій "+a+" список цілих чисел")
    try:
        smth=[int(i) for i in input().split()]
        return smth
    except ValueError:
        print("Вводьте коректні дані, будь ласка")
        return get_list(a)

    
answer=""
while answer!="stop":
    common=[]
    list_a=get_list("перший")
    list_b=get_list("другий")
    list_a.sort()
    list_b.sort()
    print("first list=",list_a)
    print("second list=",list_b)
    print("intersection between lists=",common_elems(list_a,list_b))
    answer=input("Type 'stop' if u want to stop the prog: ")
 
    
