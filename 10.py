n = int(input("Введите число - "))

print(f"Все четные делители числа {n}")
for i in range(2,n+1,2):
    if n % i == 0:
        print(i)