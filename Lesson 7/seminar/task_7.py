# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
from pathlib import Path
import send2trash

from .task_6 import gen_different_files


def sort_files(path: str | Path, groups: dict[str : list[str]] = None) -> None:
    if not groups:
        groups = {
            Path("video"): ["avi", "mov", "mk4", "mkv"],
            Path("images"): ["bmp", "jpeg", "jpg", "png"],
        }
    os.chdir(path)
    reverse_groups = {}
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for ext in ext_list:
            reverse_groups[f".{ext}"] = target_dir

    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)


if __name__ == "__main__":
    data_folder = Path("data")
    if data_folder.exists():
        send2trash.send2trash(data_folder)
    gen_different_files(
        data_folder,
        avi=2,
        doc=4,
        bin=3,
        jpg=5,
        mkv=6,
        png=3,
    )
    sort_files(Path(str(Path.cwd())))
