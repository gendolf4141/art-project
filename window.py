import customtkinter as tk
from tkinter import filedialog
from pathlib import Path
from messages import show_warning_no_directory, show_info_script_completed
from main import run_fast_scandir, rename_path, to_excel, COLUMN_TITLE
from distribution_files_in_base_path import run_distribution_files_in_base_path
from images_by_size import get_unique_values
import settings
from domain import DistributedPictures


class TabOne:
    def __init__(self, tab: tk.CTkFrame):
        self.tab = tab

        # Создание метки наименования
        self.label = tk.CTkLabel(master=self.tab, text="Скрипт 1. Переименование папок и файлов.")
        self.label.grid(row=0, columnspan=2, padx=20, pady=10)

        # Создание метки для выбора исходной папки
        self.text_choice_directory = tk.CTkLabel(self.tab, text="Исходная папка с изображениями:")
        self.text_choice_directory.grid(row=1, columnspan=2, padx=20, pady=10)

        # Создание окна выбора исходной папки
        self.entry_choice_directory = tk.CTkEntry(self.tab, width=500)
        self.entry_choice_directory.grid(row=2, columnspan=2, padx=20, pady=10)

        # Создание кнопки запуска скрипта
        self.button_choice_directory = tk.CTkButton(self.tab, text="Запустить", command=self.run_script)
        self.button_choice_directory.grid(row=3, column=0, padx=20, pady=10)

        # Создание кнопки запуска скрипта
        self.button_get_directory = tk.CTkButton(self.tab, text="Выбор папки", command=self.get_directory)
        self.button_get_directory.grid(row=3, column=1, padx=20, pady=10)

        # Создание окна лога
        self.text_log = tk.CTkTextbox(self.tab)
        self.text_log.grid(row=4, columnspan=2, padx=20, pady=10)

        self.folder_selected = None

    def log(self, message):
        self.text_log.insert('end', message + '\n')
        self.text_log.see('end')

    def run_script(self):
        if not self.folder_selected or not self.folder_selected.is_dir():
            return show_warning_no_directory()
        self.log("Скрипт запущен!")
        sub_folders, images_parameters, article = run_fast_scandir(
            self.folder_selected,
            settings.article,
            self.folder_selected.name
        )
        rename_path(images_parameters, self.folder_selected)
        to_excel(images_parameters, COLUMN_TITLE)
        for num in range(100):
            self.log(f"Тестовый лог {num}")
        self.log(show_info_script_completed())

    def get_directory(self):
        self.folder_selected = Path(filedialog.askdirectory())
        self.entry_choice_directory.insert(tk.END, self.folder_selected)


class TabTwo:
    def __init__(self, tab: tk.CTkFrame):
        self.tab = tab

        # Создание метки наименования
        self.label = tk.CTkLabel(
            master=self.tab,
            text="Скрипт 2. Распределение по папкам с соответствующими размерами."
        )
        self.label.grid(row=0, columnspan=2, padx=20, pady=10)

        # Создание метки для выбора исходного файла
        self.text_choice_directory = tk.CTkLabel(self.tab, text="Исходный файл excel:")
        self.text_choice_directory.grid(row=1, columnspan=2, padx=20, pady=10)

        # Создание окна выбора исходного файла
        self.entry_choice_directory = tk.CTkEntry(self.tab, width=500)
        self.entry_choice_directory.grid(row=2, columnspan=2, padx=20, pady=10)

        # Создание кнопки запуска скрипта
        self.button_choice_directory = tk.CTkButton(self.tab, text="Запустить", command=self.run_script)
        self.button_choice_directory.grid(row=3, column=0, padx=20, pady=10)

        # Создание кнопки получения файла
        self.button_get_excel = tk.CTkButton(self.tab, text="Выбор файла", command=self.get_excel)
        self.button_get_excel.grid(row=3, column=1, padx=20, pady=10)

        # Создание окна лога
        self.text_log = tk.CTkTextbox(self.tab)
        self.text_log.grid(row=4, columnspan=2, padx=20, pady=10)

        self.file_excel = None

    def run_script(self):
        COLUMN_TITLE = [field.description for _, field in DistributedPictures.model_fields.items()]

        if not self.file_excel or not self.file_excel.is_file():
            return show_warning_no_directory()

        self.log("Скрипт запущен!")
        images_parameters, logs = get_unique_values(self.file_excel)
        to_excel(images_parameters, COLUMN_TITLE)

        for massage in logs:
            self.log(f"Не удалось перенести {massage} из-за нехватки вводных данных")

        self.log(show_info_script_completed())

    def log(self, message):
        self.text_log.insert('end', message + '\n')
        self.text_log.see('end')

    def get_excel(self):
        self.file_excel = Path(filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")]))
        self.entry_choice_directory.insert(tk.END, self.file_excel)


class TabThree:
    def __init__(self, tab: tk.CTkFrame):
        self.tab = tab

        # Создание метки наименования
        self.label = tk.CTkLabel(
            master=self.tab,
            text="Скрипт 3. Распределение по папкам после фотошопа."
        )
        self.label.grid(row=0, columnspan=2, padx=20, pady=10)

        # Создание метки для выбора исходного файла
        self.text_choice_directory = tk.CTkLabel(self.tab, text="Исходный файл excel:")
        self.text_choice_directory.grid(row=1, columnspan=2, padx=20, pady=10)

        # Создание окна выбора исходного файла
        self.entry_choice_directory = tk.CTkEntry(self.tab, width=500)
        self.entry_choice_directory.grid(row=2, columnspan=2, padx=20, pady=10)

        # Создание кнопки запуска скрипта
        self.button_choice_directory = tk.CTkButton(self.tab, text="Запустить", command=self.run_script)
        self.button_choice_directory.grid(row=3, column=0, padx=20, pady=10)

        # Создание кнопки получения файла
        self.button_get_excel = tk.CTkButton(self.tab, text="Выбор файла", command=self.get_excel)
        self.button_get_excel.grid(row=3, column=1, padx=20, pady=10)

        # Создание окна лога
        self.text_log = tk.CTkTextbox(self.tab)
        self.text_log.grid(row=4, columnspan=2, padx=20, pady=10)

        self.file_excel = None

    def run_script(self):
        COLUMN_TITLE = [field.description for _, field in DistributedPictures.model_fields.items()]

        if not self.file_excel or not self.file_excel.is_file():
            return show_warning_no_directory()

        self.log("Скрипт запущен!")
        images_parameters, logs = run_distribution_files_in_base_path(self.file_excel)
        to_excel(images_parameters, COLUMN_TITLE)

        for massage in logs:
            self.log(f"Не удалось перенести {massage} из-за нехватки вводных данных")

        self.log(show_info_script_completed())

    def log(self, message):
        self.text_log.insert('end', message + '\n')
        self.text_log.see('end')

    def get_excel(self):
        self.file_excel = Path(filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")]))
        self.entry_choice_directory.insert(tk.END, self.file_excel)


class TabSettings:
    def __init__(self, tab: tk.CTkFrame):
        self.tab = tab

        # Создание метки "Настройки"
        self.label = tk.CTkLabel(master=self.tab, text="Настройки.")
        self.label.grid(row=0, column=0, padx=20, pady=10)

        # Создание метки для изменения артикула
        self.text_update_article = tk.CTkLabel(self.tab, text="Артикул:")
        self.text_update_article.grid(row=1, column=0, padx=20, pady=10)

        # Создание окна для изменения артикула
        self.entry_update_article = tk.CTkEntry(self.tab, width=500)
        self.entry_update_article.insert(tk.END, settings.article)
        self.entry_update_article.grid(row=2, column=0, padx=20, pady=10)

        # Создание кнопки для изменения настроек
        self.button_choice_directory = tk.CTkButton(self.tab, text="Изменить", command=self.update_settings)
        self.button_choice_directory.grid(row=3, column=0, padx=20, pady=10)

        # Создание окна лога
        self.text_log = tk.CTkTextbox(self.tab)
        self.text_log.grid(row=4, column=0, padx=20, pady=10)

    def update_settings(self):
        article = self.entry_update_article.get()
        settings.update_article_settings(article)
        self.log(message="Настройки изменены!")

    def log(self, message):
        self.text_log.insert('end', message + '\n')
        self.text_log.see('end')


class MyTabView(tk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("1")
        self.add("2")
        self.add("3")
        self.add("4")

        tab_one = TabOne(self.tab("1"))
        tab_two = TabTwo(self.tab("2"))
        tab_three = TabThree(self.tab("3"))
        tab_setting = TabSettings(self.tab("4"))


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ART PROJECT")

        label_1 = tk.CTkLabel(master=self, text="1. Переименование папок и файлов.")
        label_1.grid(row=0, column=0, padx=1, pady=1)

        label_2 = tk.CTkLabel(master=self, text="2. Распределение по папкам с соответствующими размерами.")
        label_2.grid(row=1, column=0, padx=1, pady=1)

        label_3 = tk.CTkLabel(master=self, text="3. Распределение по папкам после фотошопа.")
        label_3.grid(row=2, column=0, padx=1, pady=1)

        label_3 = tk.CTkLabel(master=self, text="4. Настройки.")
        label_3.grid(row=3, column=0, padx=1, pady=1)

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=4, column=0, padx=20, pady=20)


app = App()
app.mainloop()
