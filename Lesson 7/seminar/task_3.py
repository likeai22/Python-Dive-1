# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.

from pathlib import Path
from typing import TextIO

__all__ = [
    "sum_files",
]


def _read_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == "":
        fd.seek(0)
        text = fd.readline()
    return text.strip()


def sum_files(f1_name: str | Path, f2_name: str | Path, res_file: str | Path) -> None:
    with (
        open(f1_name, "r", encoding="UTF-8") as f1,
        open(f2_name, "r", encoding="UTF-8") as f2,
        open(res_file, "a", encoding="UTF-8") as f_res,
    ):
        len_f1 = sum(1 for _ in f1)
        len_f2 = sum(1 for _ in f2)
        for _ in range(max(len_f1, len_f2)):
            name = _read_or_begin(f1)
            num_int, num_fl = _read_or_begin(f2).split(" | ")
            mult = int(num_int) * float(num_fl)
            (
                f_res.write(f"{name.lower()} {-mult}\n")
                if mult < 0
                else f_res.write(f"{name.upper()} {int(mult)}\n") if mult > 0 else 42
            )


if __name__ == "__main__":
    sum_files(Path("names.txt"), Path("numbers.txt"), Path("results.txt"))
