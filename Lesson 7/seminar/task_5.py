# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from .task_4 import gen_files


def num_files(**kwargs) -> None:
    for ext, num in kwargs.items():
        gen_files(ext, file_count=num)


if __name__ == "__main__":
    num_files(bin=2, jpeg=1)
