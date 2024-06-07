import argparse

__all__ = ["check_data"]


def _is_leap(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def _date_is_true(data: str) -> bool:
    day, month, year = list(map(int, data.split(".")))
    check_days = {
        1: 31,
        2: 29 if _is_leap(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    max_day = check_days.get(month)
    if not max_day or (year > 9999 or year < 1) or (day > max_day or day < 1):
        return False
    else:
        return True


# Парсер аргументов коммандной строки
def _arg_parser():
    parser = argparse.ArgumentParser(description="Проверка даты.")
    parser.add_argument(
        "-d", "--date", help="Дата в формате DD.MM.YYYY", required=True, type=str
    )
    return parser


def check_data():
    # python check_date.py --date  01.01.2024
    print("Клиент модуля с проверкой даты")
    parser = _arg_parser()
    args = parser.parse_args()
    is_valid_date = _date_is_true(args.date)
    flag = "" if is_valid_date else "не "

    print(f"Дата введена {flag}правильно: {args.date}")


if __name__ == "__main__":
    check_data()
