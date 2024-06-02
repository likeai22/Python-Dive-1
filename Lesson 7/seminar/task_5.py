# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from random import choices, randint
from string import ascii_lowercase, digits


def gen_files(
    ext: str,
    min_name: int = 6,
    max_name: int = 30,
    min_size: int = 256,
    max_size: int = 4096,
    file_count: int = 42,
) -> None:
    for _ in range(file_count):
        name = "".join(
            choices(ascii_lowercase + digits + "_", k=randint(min_name, max_name))
        )
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f"{name}.{ext}", "wb") as f:
            f.write(data)


def num_files(**kwargs) -> None:
    for ext, num in kwargs.items():
        gen_files(ext, file_count=num)


if __name__ == "__main__":
    num_files(bin=2, jpeg=1)
