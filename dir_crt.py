import os

# Цикл для создания папок Lesson 1 до Lesson 8
for n in range(1, 9):
    folder_name = f'Python-Dive-1/Lesson {n}'
    os.makedirs(folder_name, exist_ok=True)
    print(f'Создана папка: {folder_name}')