"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)"""

from random import randint

num = randint(0, 1000)
for i in range(1, 11):
    my_num = int(input(f"Попытка {i}: Предполагаемоен число: "))
    if my_num < num:
        print("Загаданное число больше")
    elif my_num > num:
        print("Загаданное число меньше")
    else:
        print(f"Поздравляем! Вы угадали число {num} за {i} попыток.")
        break
else:
    print(f"Вы проиграли. Загаданное число было {num}.")


