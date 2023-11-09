# Вычислите суммы чисел: Напишите программу для вычисления суммы чисел от 1 до N.

# Императивный стиль
n = 5
summa = 0

for i in range(1, n + 1):
    summa += i

# print(f"Cумма чисел от 1 до {n} равна {summa}")

summa = 0
numbers = range(1, n +1)
# Декларативный стиль
summa = sum(numbers)
print(f"Cумма чисел от 1 до {n} равна {summa}")























