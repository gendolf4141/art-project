import os
from enum import StrEnum
from typing import Optional
import pandas as pd
from PIL import Image
import time
from .constants import TRANSLATE, NAME_COLUMNS


root_dir = input('Введите путь до родительской папки: ')
article = int(input('Введите начальное значение артикла: '))

print('Стартуем!')
time.sleep(5)


class Extension(StrEnum):
    FIFTY_BY_FIFTY = "50*50"
    FIFTY_BY_SIXTY = "50*60"
    FIFTY_BY_SEVENTY = "50*70"
    FIFTY_BY_EIGHTY = "50*80"
    FIFTY_BY_NINETY = "50*90"
    FIFTY_BY_ONE_HUNDRED = "50*100"


class Orientation(StrEnum):
    HORIZONTAL = "Горизонтальные"
    VERTICAL = "Вертикальные"
    SQUARE = "Квадратные"


def get_extension_by_coefficient(value: Optional[int, float]) -> Extension:
    if 1 <= value <= 1.1:
        return Extension.FIFTY_BY_FIFTY
    elif 1.100000001 <= value <= 1.3:
        return Extension.FIFTY_BY_SIXTY
    elif 1.300000001 <= value <= 1.5:
        return Extension.FIFTY_BY_SEVENTY
    elif 1.500000001 <= value <= 1.7:
        return Extension.FIFTY_BY_EIGHTY
    elif 1.700000001 <= value <= 1.9:
        return Extension.FIFTY_BY_NINETY
    elif 1.900000001 <= value <= 5:
        return Extension.FIFTY_BY_ONE_HUNDRED


def check_orientation(width_value: Optional[int, float], height_value: Optional[int, float]) -> Orientation:
    max_value = max(width_value, height_value)
    min_value = min(width_value, height_value)

    if 1 <= round(max_value / min_value, 3) < 1.1:
        return Orientation.SQUARE
    elif width_value == max_value:
        return Orientation.HORIZONTAL
    else:
        return Orientation.VERTICAL


def translate(text: str) -> str:
    text_translate = ''
    for letter in text.lower():
        if letter in TRANSLATE:
            text_translate += TRANSLATE[letter]
        else:
            text_translate += letter
    return text_translate


result_row: list[tuple] = []


for root_dir_name in os.listdir(root_dir):
    root_dir_name_translate = translate(root_dir_name).replace(' ', '-')
    path_root_dir_name_translate = os.path.join(root_dir, root_dir_name_translate)
    os.rename(os.path.join(root_dir, root_dir_name), path_root_dir_name_translate)

    for dir_name in os.listdir(path_root_dir_name_translate):
        dir_name_translate = translate(dir_name).replace(' ', '-')
        path_dir_name = os.path.join(path_root_dir_name_translate, dir_name_translate)
        os.rename(os.path.join(path_root_dir_name_translate, dir_name), path_dir_name)

        for count, name_file in enumerate(os.listdir(path_dir_name), start=1):
            new_name_file = f'{dir_name_translate}-{count}.{name_file.split(".")[-1]}'
            path_new_name_file = os.path.join(path_dir_name, new_name_file)
            os.rename(os.path.join(path_dir_name, name_file), path_new_name_file)

            im = Image.open(path_new_name_file)
            width, height = im.size
            coefficient = round(max(width, height) / min(width, height), 3)

            new_name_file_with_article = f'{dir_name} Арт.{article}'

            size_img = get_extension_by_coefficient(coefficient)

            categoty = f'Картины > {root_dir_name} > {dir_name}'

            url_img = f'https://liss-art.ru/wp-content/uploads/img-product1/{root_dir_name_translate}/{dir_name_translate}/{new_name_file}'

            orientation = check_orientation(width, height)

            result_row.append((root_dir_name, dir_name, root_dir_name_translate, dir_name_translate, path_dir_name, new_name_file, width, height, coefficient, new_name_file_with_article, size_img, article, categoty, url_img, orientation))

            article += 1

result_df = pd.DataFrame(result_row, columns=NAME_COLUMNS)
result_df.to_excel(os.path.join(os.path.dirname(root_dir), 'Result.xlsx'), index=False)
print("Завершение программы")