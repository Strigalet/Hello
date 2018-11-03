print("============================================")
print("            ЛАБОРАТОРНА РОБОТА №2")
print("     ПРОГРАМУВАННЯ ЦИКЛІЧНИХ АЛГОРИТМІВ")
print("    АВТОР: КАСІЧ БОГДАН , КМ-83 (6 ВАРІАНТ)")
print("============================================")
print(" Добрий день!!! Дана програма знайде суму значень виразу (x-i)/i**2 в залежності від введеного вами числа x")
print(" та значень натурального числа i , яке належить проміжку від 1 до введеного вами n")
print(" Програма написана за допомогою оператор for")


while True:
    try:
        x=float(input("Введіть будь-яке число x:  "))
    except ValueError:
        print("Введiть коректнi данi")
        continue
    while True:
        try:
            n=int(input("Введіть натуральне число n:  "))
        except ValueError:
            print("Введiть коректнi данi")
            continue
    
 
         
        
        sum=0

        for i in range(0,n):
            i += 1
            sum += (x-i)/i**2
        if n >= 1:    
            print(sum)
            break
        else:
            print("Введіть коректні дані")
            continue
        
    
    answer=input("Print 'Not' if u want to break: " )
    if answer == "Not":
        break
    else:
        continue
