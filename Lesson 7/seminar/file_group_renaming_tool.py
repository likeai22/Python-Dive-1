import os
from pathlib import Path
from shutil import move

import send2trash

from task_6 import gen_different_files


def file_group_renaming_tool(
        digits_count: int,
        ext: str,
        new_ext: str,
        file_range: list,
        new_file_name: str = "",
        path: str | Path = Path("data"),
) -> None:
    data_folder = path

    data_files = list(data_folder.glob(f"*.{ext}"))
    name_slice = slice(file_range[0], file_range[1])

    for num, data_file in enumerate(data_files):
        if data_file.is_file():
            old_name = (
                data_file.stem[name_slice]
                if file_range[1] <= len(data_file.stem)
                else len(data_file.stem)
            )
            new_file_path = os.path.join(
                data_folder,
                f"{old_name}{new_file_name}{num + 1:0{digits_count}}.{new_ext}",
            )
            move(data_file, new_file_path)
            print(
                f"Новое имя файла после преобразования: {old_name}{new_file_name}{num + 1:0{digits_count}}.{new_ext}"
            )
        else:
            print(f"Файл {data_file} не существует.")


if __name__ == "__main__":
    data_folder = Path("../data")
    if data_folder.exists():
        send2trash.send2trash(data_folder)
    gen_different_files(
        data_folder,
        doc=5,
        bin=3,
    )
    file_group_renaming_tool(6, "doc", "csv", [0, 3], "resume")
