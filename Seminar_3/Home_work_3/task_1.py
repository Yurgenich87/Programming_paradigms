def check_winner(array, player):
    # Условия победы для строк, столбцов и диагоналей
    win_conditions = [
        [[0, 0], [0, 1], [0, 2]],  # Верхний ряд
        [[1, 0], [1, 1], [1, 2]],  # Средний ряд
        [[2, 0], [2, 1], [2, 2]],  # Нижний ряд
        [[0, 0], [1, 0], [2, 0]],  # Левый столбец
        [[0, 1], [1, 1], [2, 1]],  # Средний столбец
        [[0, 2], [1, 2], [2, 2]],  # Правый столбец
        [[0, 0], [1, 1], [2, 2]],  # Диагональ слева направо
        [[0, 2], [1, 1], [2, 0]]   # Диагональ справа налево
    ]

    # Проверка всех условий победы
    for condition in win_conditions:
        marks = [array[row][col] for row, col in condition]
        if all(mark == player for mark in marks):
            return True
    return False


def print_board(array):
    # Печать текущего состояния игровой доски
    for row in array:
        print(' '.join(row))


def play_game():
    # Создание пустой игровой доски
    letters = [['-' for _ in range(3)] for _ in range(3)]
    print_board(letters)

    player = 'x'
    while True:
        print(f"Ход {player}:")
        row_index = int(input("Введите номер строки(от 1 до 3): ")) - 1
        column_index = int(input("Введите номер столбца(от 1 до 3): ")) - 1

        # Проверка на доступность клетки и установка символа игрока
        if letters[row_index][column_index] == '-':
            letters[row_index][column_index] = player
        else:
            print("Эта клетка уже занята. Попробуйте снова.")
            continue

        print_board(letters)

        # Проверка победы игрока
        if check_winner(letters, player):
            print(f"<<< Выйграли {player} >>>")
            break

        # Проверка на ничью
        draw = all(mark != '-' for row in letters for mark in row)
        if draw:
            print("<<< Ничья >>>")
            break

        # Смена игрока
        player = 'o' if player == 'x' else 'x'

    print("Игра завершена.")


if __name__ == "__main__":
    play_game()
