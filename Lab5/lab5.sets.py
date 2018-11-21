print("""
        ===================================================================
                              ЛАБОРАТНОРНА РОБОТА №5
                    СТРУКТУРИ ДАНИХ: СПИСКИ,КОРТЕЖИ, МНОЖИНИ
                             (РОБОТА ІЗ МНОЖИНАМИ)
                     АВТОР: КАСІЧ БОГДАН, КМ-83 (6 ВАРІАНТ)    
        ===================================================================
Добрий день! Дана програма виведе вам усі вказані в завданні операції над двома даними множинами A і B.
(об'єднання,перетин,різниця,симетрична різниця,доповнення,декартовий добуток та індивідуальне завдання)

                                                                                 """)

import itertools
A={1,2,"ee","a","d"}
B={1,"d","tt",4,3}
Univers={1,2,3,4,"a","b","c","d","ee","tt","ww"}
uni=A.union(B)            
intersect=A.intersection(B)  
diff_A_B=A.difference(B)
diff_B_A=B.difference(A)
symm_diff=A.symmetric_difference(B)
addition_A=Univers.difference(A)
addition_B=Univers.difference(B)
C=set()
G=set()

print("==============================")
print("A=",A)
print("B=",B)
print("==============================")
print("A U B=", uni)
print("==============================")
print("A П B=", intersect)
print("==============================")
print("A / B=", diff_A_B)
print("==============================")
print("B / A=", diff_B_A)
print("==============================")
print("A + B=", symm_diff)
print("==============================")
print("A'=", addition_A)
print("==============================")
print("B'=", addition_B)
print("==============================")
print("(A U B) П (A / B)=",uni.intersection(diff_A_B))
print("==============================")
for i in itertools.product(A,B):
    C.add(i)
print("A X B=",C)
print("==============================")
for i in itertools.product(B,A):
   G.add(i)
print("B X A=",G)

input("Програму завершено")
