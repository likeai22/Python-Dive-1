# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
from pathlib import Path
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
    data_folder = Path("data")
    data_folder.mkdir(parents=True, exist_ok=True)

    for _ in range(file_count):
        name = "".join(
            choices(ascii_lowercase + digits + "_", k=randint(min_name, max_name))
        )
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))

        with open(Path.cwd() / f"{data_folder}" / f"{name}.{ext}", "wb") as f:
            f.write(data)


if __name__ == "__main__":
    gen_files("bin", file_count=5)
