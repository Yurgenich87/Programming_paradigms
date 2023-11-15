"""Переписать алгоритм в процедурном стиле
Структурное программирование

Определение функции merge_sort, которая выполняет сортировку методом слияния.
"""

"""
def merge_sort(arr):
    if len(arr) > 1:  # Проверка, что длина массива больше 1 (иначе сортировка не нужна).
        mid = len(arr) // 2  # Вычисление середины массива.
        left_half = arr[:mid]  # Создание левой половины массива.
        right_half = arr[mid:]  # Создание правой половины массива.
        # Рекурсивный вызов merge_sort для левой и правой половин массива.
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0  # Инициализация индексов для объединения двух половин.

        # Объединение левой и правой половин в один отсортированный массив.
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:  # Сравнение элементов левой и правой половин.
                arr[k] = left_half[i]  # Если элемент из левой меньше, помещаем его в исходный массив.
                i += 1
            else:
                arr[k] = right_half[j]  # Если элемент из правой меньше, помещаем его в исходный массив.
                j += 1
            k += 1

        # Добавление оставшихся элементов из левой и правой половин (если такие есть).
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


my_array = [64, 34, 25, 12, 22, 11, 90]  # Создание неотсортированного массива.
merge_sort(my_array)  # Вызов функции сортировки слиянием.
print("Отсортированный массив (Merge Sort):", my_array)  # Вывод отсортированного массива.
"""


# Функция для слияния отсортированных списков left_half и right_half в список arr.
def merge(arr, left_half, right_half):
    i = j = k = 0

    # Слияние элементов из left_half и right_half в список arr.
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:  # Если элемент из left_half меньше, добавляем его в arr.
            arr[k] = left_half[i]
            i += 1
        else:  # Если элемент из right_half меньше или равен, добавляем его в arr.
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Добавление оставшихся элементов из left_half в arr.
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Добавление оставшихся элементов из right_half в arr.
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


# Функция сортировки слиянием.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]   # Создание левой половины массива.
        right_half = arr[mid:]  # Создание правой половины массива.

        merge_sort(left_half)   # Рекурсивный вызов merge_sort для левой половины.
        merge_sort(right_half)  # Рекурсивный вызов merge_sort для правой половины.

        merge(arr, left_half, right_half)  # Слияние отсортированных половин.


my_array = [64, 34, 25, 12, 22, 11, 90]  # Создание неотсортированного массива.

merge_sort(my_array)  # Вызов функции сортировки слиянием.
print("Отсортированный массив (Merge Sort):", my_array)  # Вывод отсортированного массива.

