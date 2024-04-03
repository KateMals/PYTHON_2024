# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.


n = int(input("n = :"))
e = int(input("e = :"))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0 and i % e != 0:
        sum = sum + i
print(sum)

