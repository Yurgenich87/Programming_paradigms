import numpy as np

def pearson_correlation(x, y):
    """Принимает два массива x и y."""
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    std_dev_x = np.std(x)
    std_dev_y = np.std(y)

    # Проверка на нулевое стандартное отклонение:
    if std_dev_x == 0 or std_dev_y == 0:
        return 0  # если стандартное отклонение одного из массивов равно нулю, корреляция равна 0

    correlation = np.sum((x - mean_x) * (y - mean_y)) / (len(x) * std_dev_x * std_dev_y)
    return correlation

# Пример данных (два случайных массива)
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

# Рассчитываем корреляцию Пирсона
result = pearson_correlation(array1, array2)
print(f"Корреляция Пирсона: {result}")
