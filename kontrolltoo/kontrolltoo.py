#d=''
#i=''
#while d not in[1,2,3,4,5,6,7,8,9]:
#    try:
#        d=int(input("Сколько зверьков показать (от 1 до 9): "))
#    except ValueError:
#        print("Напишите число от 1 до 9: ")
#for i in range(d):
#    print(' ^---^ ', end=(" "))
#print()
#for i in range(d):
#    print('( o o )', end=(" "))
#print()
#for i in range(d):
#    print('! = !/)', end=(" "))
#print()


#p = int(input("Показатель степени: "))
#n = int(input("Предел: "))
#i = 1
#while i**p<=n:
#    print(i**p,end=(' '))
#    i+=1
#print("\nПоследнее число,", "возведенное в степень:", i - 1)

#i = 0
#k = 1
#while i <= 24:
# k *= 3
# print(k)
# i += 3

from random import *
max=0
min=5
k=randint(1,27)
for i in range(k):
    ocenka=randint(1,5)
    if ocenka<5:
        ocenka=ocenka+random()
        ocenka=round(ocenka)
    print(ocenka, end=" ")
    if ocenka>max:
        max=ocenka
    if ocenka<min:
        min=ocenka
print()
print("Минимальная оценка: ", min)
print("Максимальная оценка: ", max)
 
 
#a=0
#K=int(input("Сколько котлет у тебя есть? --> "))
#M=int(input("Сколько котлет помещается на сковородку? --> "))
#for i in range(K):
#    a=K//M
#print()
#print(f"Понадобится {a} сковородки ")
#for i in range(K):
#    b=K%M
#print(f"Останется сделать {b} котлет ")
#print()
