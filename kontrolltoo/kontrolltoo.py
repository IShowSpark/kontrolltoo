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

#from random import *
#maxOcenka=0
#minOcenka=5
#kolvo=randint(1,27)
#for i in range(kolvo):
#    ocenka=randint(1,5)
#    if ocenka<5:
#        ocenka=ocenka+random()
#        ocenka=round(ocenka)
#    print(ocenka, end=" ")
#    if ocenka>maxOcenka:
#        maxOcenka=ocenka
#    if ocenka<minOcenka:
#        minOcenka=ocenka
#print()
#print("Минимальная оценка: ", minOcenka)
#print("Максимальная оценка: ", maxOcenka)
 
 
a=0
K=int(input("Сколько котлет у тебя есть? --> "))
M=int(input("Сколько котлет помещается на сковородку? --> "))
for i in range(K):
    a=K//M
print()
print(f"Понадобится {a} сковородки ")
for i in range(K):
    b=K%M
print(f"Останется сделать {b} котлет ")
print()

