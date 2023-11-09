from Seminar_1.Home_work_1.task_1 import sort_list_imperative
from Seminar_1.Home_work_1.task_2 import sort_list_declarative

if __name__ == '__main__':
    numbers = [5, 2, 9, 1, 5, 6]
    sorted_imperative = sort_list_imperative(numbers.copy())
    sorted_declarative = sort_list_declarative(numbers.copy())

    print("Императивный стиль:", sorted_imperative)
    print("Декларативный стиль:", sorted_declarative)
