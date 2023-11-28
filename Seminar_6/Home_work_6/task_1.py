def binary_search(arr, target):
    """Метод для бинарного поиска"""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Пример использования функции:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = binary_search(arr, target)

if result != -1:
    print(f"Элемент {target} найден в индексе {result}")
else:
    print(f"Элемент {target} не найден в массиве")
