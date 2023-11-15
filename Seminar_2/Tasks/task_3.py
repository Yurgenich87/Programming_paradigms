def bibble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Тестировании функции

if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", test_array)

    bibble_sort(test_array)
    print("Отсортированный массив:", test_array)
