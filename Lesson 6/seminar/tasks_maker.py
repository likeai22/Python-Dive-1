import datetime
from pathlib import Path

QUANTITY = 8


def tasks_maker(data_folder: str | Path):
    extensions = [
        "py",
    ]
    now = datetime.datetime.now()
    date_time_str = now.strftime("%d %b %Y %H:%M")

    for file in range(1, QUANTITY):
        for ext in extensions:
            file_name = f"task_{file}.{ext}"
            file_path = data_folder / file_name
            with open(file_path, "w") as f:
                f.write(f"# github.com/likeai22 {file_name} {date_time_str}.")
    return data_folder


if __name__ == "__main__":
    tasks_maker(Path.cwd())
