n = int(input("Кол-во первых членов прогрессии - "))
a = int(input("Начальный член прогрессии - "))
r = int(input("Знаменатель - "))

for i in range(1,n+1):
    an = a * r**(i-1)
    print(an)