n = int(input("Введите число - "))
sumchet = 0
sumnechet = 0

for i in range(n+1):
    if i % 2 == 0:
        sumchet += 1
    else:
        sumnechet += 1
print(f'Всего четных чисел - {sumchet}')
print(f'Всего нечетных чисел - {sumnechet}')
