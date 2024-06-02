# Напишите функцию, которая генерирует
# псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from pathlib import Path
from random import randint, choice

MIN_VALUE = 4
MAX_VALUE = 7
VOWELS = "eyuioa"
CONSONANTS = "qwrtpsdfghjklzxcvbnm"


def gen_names(str_counts: int, file_name: str | Path) -> None:
    with open(file_name, "a", encoding="UTF-8") as f:
        for _ in range(str_counts):
            name = ""
            flag = choice([-1, 1])
            for _ in range(randint(MIN_VALUE, MAX_VALUE)):
                if flag == -1:
                    name += choice(CONSONANTS)
                else:
                    name += choice(VOWELS)
                flag *= -1
            f.write(name.title() + "\n")


if __name__ == "__main__":
    gen_names(10, Path("names.txt"))
