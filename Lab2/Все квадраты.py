print("============================================")
print("            ЛАБОРАТОРНА РОБОТА №2")
print("     ПРОГРАМУВАННЯ ЦИКЛІЧНИХ АЛГОРИТМІВ")
print("    АВТОР: КАСІЧ БОГДАН , КМ-83 (6 ВАРІАНТ)")
print("============================================")
print(" Добрий день!!! Дана програма виведе квадрати усіх натуральних чисел, ")
print(" якi не перевищують введеного вами числа n ")
print(" Програма написана за допомогою цикла while ")


while True:
    try:
        n=float(input("Введiть ваше число n: "))
    except ValueError:
        print("Введiть коректнi данi")
        continue

    i=1
    

    while (i*i) <= n:
        print(i*i)
        i += 1
   

    answer=input("Print 'Not' if u want to break: ")
    if answer=="Not":
        break
    else:
        continue

