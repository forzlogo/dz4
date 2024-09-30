n = int(input("Введите число от 100 до 999 - "))

if 100<n<1000:
    for i in range(101,n+1):
        a = i // 100
        b = (i % 100) //10
        c = i % 10
        if a == c:
            print(a,b,c)
else:
    print("Введите число от 100 до 999")