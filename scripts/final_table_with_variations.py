from pathlib import Path
from openpyxl import load_workbook
from domain import FinalTable
from constants import VARIATIONS


def read_excel(file_excel: Path):
    workbook = load_workbook(filename=file_excel)
    sheet = workbook["Страница"]
    return sheet.iter_rows(min_row=2, values_only=True)


def run_final_table_with_variations(file_excel: Path):
    data = read_excel(file_excel)
    final_tables = []
    logs = []
    for row in data:
        final_tables_dict = {}
        for i, key in enumerate(FinalTable.__fields__.keys()):
            if row[i] is not None:
                final_tables_dict[key] = row[i]

        final_table = FinalTable(**final_tables_dict)

        variations = VARIATIONS.get(final_table.id)

        if variations:
            for variation in variations:
                final_table.base_price = variation(0)
                final_table.position = variation(1)
                final_table.attribute_values_1 = variation(2)

    return final_tables, logs
