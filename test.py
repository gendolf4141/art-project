import time

import pandas as pd
import os
from pathlib import Path

PROJECT: Path = Path(r"C:\Users\Public\Documents")
file_name: Path = Path(os.path.join(PROJECT, "exsample.xlsx"))


def read_type_img(value) -> pd.DataFrame:
    read_type = pd.read_excel(file_name, sheet_name="Вариации")
    check_list = read_type[read_type.ID == value]
    return check_list


def read_final() -> pd.DataFrame:
    read_final_data = pd.read_excel(file_name, sheet_name="Исходная таблица")
    return read_final_data


def create_file(dataframe: pd.DataFrame) -> list:
    result_df = []
    for row in dataframe.values:
        name_img = row[3]
        perent = row[2]
        articl = "15"
        if row[40] == "30x40, 40x60, 50x70, 60x80":
            page = read_type_img("50*70")
            page["Имя"] = name_img
            page["Родительский"] = perent
            page["Артикул"] = page["Родительский"].astype(str) + "-" + page["Позиция"].astype(str)

            result_df.append(row)
            for i in page.values:
                result_df.append(i)
        elif row[40] == "30x40, 40x50, 50x60, 60x70":
            page = read_type_img("50*60")
            page["Имя"] = name_img
            page["Родительский"] = perent
            page["Артикул"] = page["Родительский"].astype(str) + "-" + page["Позиция"].astype(str)

            result_df.append(row)
            for i in page.values:
                result_df.append(i)

        elif row[40] == "30x30, 40x40, 50x50, 60x60":
            page = read_type_img("50*50")
            page["Имя"] = name_img
            page["Родительский"] = perent
            page["Артикул"] = page["Родительский"].astype(str) + "-" + page["Позиция"].astype(str)

            result_df.append(row)
            for i in page.values:
                result_df.append(i)
    return result_df



def main():
    print("Начинаю собирать файл, жди...")
    finaf_df = read_final()
    result_list = create_file(finaf_df)
    finall = pd.DataFrame(result_list, columns=finaf_df.columns)
    way_result_file: Path = Path(os.path.join(PROJECT, "teams.xlsx"))
    finall.to_excel(way_result_file, sheet_name="board", index=False)
    print("Все, забирай свой файл!")
    time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()