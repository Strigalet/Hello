print("============================================")
print("            ЛАБОРАТОРНА РОБОТА №3")
print("         РЯДКИ ТА ОПЕРАЦІЇ НАД НИМИ")
print("    АВТОР: КАСІЧ БОГДАН , КМ-83 (6 ВАРІАНТ)")
print("============================================")
print(" Драстуйте! Дана программа дозволить вам ввести певне речення та задати максимальну довжину слова")
print(" Кожне слово буде доповнено символом '*' , якщо його довжина менше заданої , до заданої довжини")

from string import punctuation
while True:
    try:
        lenght=int(input("Задайте максимальну довжину слова: "))
    except ValueError:
        print("Введіть корректні дані")
        continue
    if lenght <= 0:
        print("Введіть корректні дані")
        continue
    s=[str(i) for i in input("Введіть ваше речення: ").split()]
    print("Ваш результат:")
    for a in s:
        while len(a) < lenght and a not in punctuation:
            a=a+"*"
        print(a,end=" ")

        
    answer=input("\nВведіть 'stop' , щоб завершити програму: ")
    if answer=="stop":
      break
    else:
      continue

 
        



