# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    numbers = [5, 2, 9, 1, 5, 6]
    sorted_imperative = sort_list_imperative(numbers.copy())
    sorted_declarative = sort_list_declarative(numbers.copy())

    print("Императивный стиль:", sorted_imperative)
    print("Декларативный стиль:", sorted_declarative)


