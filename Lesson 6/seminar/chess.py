import argparse
import random
import sys

__all__ = ["chess_user_interactive", ]


def _horn(d, n):
    """Реализация схемы Горнера."""
    n1 = n + 1
    fn = float(n)
    s1 = 0.0
    s2 = 0.0
    for i in range(n):
        n1i = n1 - i - 2
        s1 = s1 * fn + float(d[i])
        s2 = s2 * fn + float(d[n1i])
    return min(s1, s2)


def _solve_n_queens_util(board, col):
    """Рекурсивно решает задачу о восьми ферзях."""
    if col >= len(board):
        return [_board_copy(board)]

    solutions = []
    for i in range(len(board)):
        if _is_safe(board, row=i, col=col):
            board[i][col] = 1
            solutions += _solve_n_queens_util(board, col + 1)
            board[i][col] = 0

    return solutions


def _is_safe(board, row=None, col=None, positions=None, k=None):
    """Проверяет, можно ли безопасно поставить ферзя.

    Аргументы:
    board -- матрица доски
    row, col -- позиция ферзя на доске
    positions -- список позиций ферзей
    k -- индекс ферзя в списке позиций
    """
    if board is not None:
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

    elif positions is not None and k is not None:
        for j in range(k):
            if (
                    positions[k] == positions[j]
                    or abs(positions[k] - positions[j]) == k - j
            ):
                return False

    return True


def _board_copy(board):
    """Создает копию доски."""
    return [row[:] for row in board]


def _solve_n_queens(n=8):
    """Решает задачу о восьми ферзях и выводит 12 уникальных решений."""
    all_solutions = _solve_n_queens_util([[0] * n for _ in range(n)], 0)
    unique_solutions = []
    solutions = []

    for solution in all_solutions:
        solutions.append(_solution_to_positions(solution))

    for d in solutions:
        if _is_unique_solution_number(d, unique_solutions, n):
            unique_solutions.append(d)
            if len(unique_solutions) == 12:
                break

    return all_solutions, unique_solutions


def _solve_n_queens_horn(n=8):
    """Решает задачу о восьми ферзях и выводит уникальные решения."""
    d = [0] * n
    all_solutions = _solve_n_queens_util([[0] * n for _ in range(n)], 0)
    unique_solutions = []
    i = 0

    while True:
        if i == n:
            if d[n - 1] < d[0]:
                i = n - 1
            else:
                dd = [9 - d[j] for j in range(n)]
                dg = [0] * n
                for j in range(n):
                    r = d[j]
                    l = 9 - r
                    dg[l - 1] = j + 1
                x = _horn(dd, n)
                y = _horn(dg, n)
                z = _horn(d, n)

                # unique_solutions.append(d[:])

                if x >= z and y >= z:
                    unique_solutions.append(d[:])
                i = n - 1

        if i < 0:
            break

        if d[i] < n:
            d[i] += 1
            if _is_safe(None, positions=d, k=i):
                i += 1
            else:
                continue
        else:
            d[i] = 0
            i -= 1

    return all_solutions, unique_solutions


def _solution_to_positions(board):
    """Преобразует доску в список позиций ферзей."""
    positions = []
    for col in range(len(board)):
        for row in range(len(board)):
            if board[row][col] == 1:
                positions.append(row + 1)
                break
    return positions


def _is_unique_solution_number(d, unique_numbers, n):
    """Проверяет, является ли решение уникальным с учётом симметрий."""
    transformations = _generate_all_transformations_number(d, n)
    for unique in unique_numbers:
        if tuple(unique) in transformations:
            return False
    return True


def _generate_all_transformations_number(d, n):
    """Генерирует все уникальные трансформации списка позиций (повороты и отражения)."""
    transformations = set()
    current = d
    for _ in range(4):
        current = _rotate_90_positions(current, n)
        transformations.add(tuple(current))
        transformations.add(tuple(_mirror_positions(current, n)))
    return transformations


def _rotate_90_positions(d, n):
    """Поворачивает список позиций ферзей на 90 градусов."""
    new_d = [0] * n
    for i in range(n):
        new_d[i] = d.index(i + 1) + 1
        # new_d[i] = n - d[i] + 1
    return new_d[::-1]


def _mirror_positions(d, n):
    """Зеркально отражает список позиций ферзей."""
    return [n - x + 1 for x in d]


def _random_queen_positions(n=8):
    """Генерирует случайную расстановку ферзей на доске."""
    positions = list(range(1, n + 1))
    random.shuffle(positions)
    return positions


def _check_random_solutions(n=8, count=4):
    """Генерирует случайные расстановки ферзей и проверяет их на корректность."""
    valid_solutions = []
    attempts = 0

    while len(valid_solutions) < count and attempts < 1000:
        attempts += 1
        d = _random_queen_positions(n)
        if _is_valid_solution(d):
            valid_solutions.append(d)

    for solution in valid_solutions:
        _print_solution(solution, data_type="positions")


def _is_valid_solution(d):
    """Проверяет, является ли случайная расстановка ферзей корректной."""
    for k in range(len(d)):
        if not _is_safe(None, positions=d, k=k):
            return False
    return True


def _print_solution(data, data_type="board"):
    """Печатает решение в виде строки и координат."""
    if data_type == "board":
        board = data
        for row in board:
            print(" ".join("Q" if x else "." for x in row))
        print()
        coordinates = _solution_to_positions(board)
    elif data_type == "positions":
        coordinates = data
        n = len(coordinates)
        board = [["." for _ in range(n)] for _ in range(n)]
        for i in range(n):
            board[coordinates[i] - 1][i] = "Q"
        for row in board:
            print(" ".join(row))
        print()
    print(f"Решение (строка) {' '.join(map(str, coordinates))}")


def _check_custom_positions():
    """Проверяет пользовательские координаты ферзей."""
    try:
        print("Введите координаты ферзей (формат: x1 y1, x2 y2, ..., x8 y8):")
        positions = input().strip().split(",")
        positions = [(int(x.split()[0]), int(x.split()[1])) for x in positions]
        if len(positions) != 8:
            raise ValueError("Неверное количество координат.")

        rows = [x[0] for x in positions]
        cols = [x[1] for x in positions]

        if not (all(1 <= x <= 8 for x in rows) and all(1 <= x <= 8 for x in cols)):
            raise ValueError("Координаты должны быть в диапазоне от 1 до 8.")

        if len(set(rows)) != 8 or len(set(cols)) != 8:
            raise ValueError("Координаты должны быть уникальными для каждого ферзя.")

        d = [0] * 8
        for i in range(8):
            d[cols[i] - 1] = rows[i]

        if _is_valid_solution(d):
            print("Данная расстановка ферзей является корректным решением.")
            return True
        else:
            print("Данная расстановка ферзей не является корректным решением.")
            return False
    except Exception as e:
        print(f"Ошибка: {e}. Попробуйте снова.")

    # (1 6, 2 1, 3 4, 4 7, 5 3, 6 8, 7 2, 8 5) неверно
    # (1 3, 2 6, 3 2, 4 5, 5 8, 6 1, 7 7, 8 4) верно


def _print_help():
    """Выводит справку по использованию."""
    print("Меню:")
    print("1. Показать все 92 решения")
    print("2. Показать 12 уникальных решений трансформацией")
    print("3. Показать 12 уникальных решений используя схему Горнера")
    print("4. Генерировать случайные расстановки и проверить их")
    print("5. Проверить свои пары чисел, каждое число от 1 до 8 - координаты 8 ферзей")
    print("6. Выход")


def user_interactive():
    """Функция взаимодействия с пользователем, запрашивает команды,
    отправляет результат работы на экран."""
    _print_help()
    while True:
        choice = input("Выберите опцию (1-6): ")
        if choice == "1":
            all_solutions, _ = _solve_n_queens()
            for solution in all_solutions:
                _print_solution(solution, data_type="board")
        elif choice == "2":
            _, unique_solutions = _solve_n_queens()
            for solution in unique_solutions:
                _print_solution(solution, data_type="positions")
        elif choice == "3":
            _, unique_solutions = _solve_n_queens_horn()
            for solution in unique_solutions:
                _print_solution(solution, data_type="positions")
        elif choice == "4":
            _check_random_solutions()
        elif choice == "5":
            _check_custom_positions()
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def chess_user_interactive():
    print("Клиентский модуль задачи о 8 ферзях.")
    user_interactive()
    return 0


if __name__ == "__main__":
    sys.exit(chess_user_interactive())
