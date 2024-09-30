n = int(input("kol-vo dorog - "))
t = 0

for i in range(1,n+1):
    dd = int(input(f"dlina dorogi {i} (в км) - "))
    ss = int(input(f"srednyaya skorost na doroge {i} (в км/ч) - "))
    t += dd/ss
print(f'Поездка займет {t} часов')
