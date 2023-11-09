# У вас есть список чисел, ваша задача отсортировать его по возрастанию.


# Декларативный стиль
# list_up_1 = [3, 5, 4, 1, 2]
# list_up_1.sort()
# print(list_up_1)

# Императивный стиль
list2 = [3, 5, 4, 1, 2]
n = len(list2)

for i in range(0, n - 1):
    for j in range(0, n - i - 1):
        if list2[j] > list2[j + 1]:
            list2[j], list2[j + 1] = list2[j + 1], list2[j]

print(f"Отсортированный список: {list2}")

