# github.com/likeai22 process_directory.py 07 Jun 2024 08:12.

import json
import csv
import pickle
from pathlib import Path


def process_directory(root_directory_path: str | Path) -> None:
    """Использую для задачи pathlib, но при необходимости код можно переписать для os.walk()"""
    root_directory = Path(root_directory_path)
    data = []

    for path_object in root_directory.rglob("*"):
        if path_object.is_file():
            file_data = {
                "name": path_object.name,
                "parent": path_object.parent.name,
                "size": path_object.stat().st_size,
                "type": "file",
            }
            data.append(file_data)
        elif path_object.is_dir():
            dir_size = sum(path.stat().st_size for path in path_object.rglob("*"))
            dir_data = {
                "name": path_object.name,
                "parent": path_object.parent.name,
                "size": dir_size,
                "type": "directory",
            }
            data.append(dir_data)

    with open("output.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    with open("output.csv", "w", newline="") as csv_file:
        fieldnames = ["name", "parent", "size", "type"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)

    with open("output.pickle", "wb") as pickle_file:
        pickle.dump(data, pickle_file)
