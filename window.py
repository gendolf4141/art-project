import customtkinter as tk
from tkinter import filedialog
from pathlib import Path
from messages import show_warning_no_directory, show_info_script_completed
from scripts.rename_files_and_dirs import run_rename_files_and_dirs, rename_path, to_excel
from scripts.distribution_after_photoshop import run_distribution_files_in_base_path
from scripts.distribution_by_size import get_unique_values
from scripts.final_table_without_variations import run_final_table_without_variations
from scripts.final_table_with_variations import run_final_table_with_variations
from scripts.repeat_images import run_repeat_images
import settings
from domain import DistributedPictures, ImageParameters, FinalTable, RepeatImages
from abc import abstractmethod


class BaseTab:
    def __init__(self, tab: tk.CTkFrame, base_model, name_script: str, name_file: str, text_log: tk.CTkTextbox):
        self.tab = tab
        self.name_script = name_script
        self.name_file = name_file
        self.base_model = base_model
        self.columns_title = [field.description for _, field in self.base_model.model_fields.items()]
        self.text_log = text_log

        # Создание метки наименования
        self.label = tk.CTkLabel(master=self.tab, text=name_script)
        self.label.grid(row=0, columnspan=2, padx=20, pady=10)

        # Создание метки для выбора исходного файла
        self.label_get_file = tk.CTkLabel(self.tab, text="Исходный файл excel:")
        self.label_get_file.grid(row=1, columnspan=2, padx=20, pady=10)

        # Создание окна выбора исходного файла
        self.entry_get_file = tk.CTkEntry(self.tab, width=500)
        self.entry_get_file.grid(row=2, columnspan=2, padx=20, pady=10)

        # Создание кнопки запуска скрипта
        self.button_run = tk.CTkButton(self.tab, text="Запустить", command=self.run_script)
        self.button_run.grid(row=3, column=0, padx=20, pady=10)

        # Создание кнопки получения файла
        self.button_get_file = tk.CTkButton(self.tab, text="Выбор файла", command=self.get_excel)
        self.button_get_file.grid(row=3, column=1, padx=20, pady=10)

        self.file_excel = None

    @abstractmethod
    def script(self, file_excel: Path):
        pass

    def run_script(self):
        if not self.file_excel or not self.file_excel.is_file():
            return show_warning_no_directory()

        self.log("Скрипт запущен!")
        images_parameters, logs = self.script(self.file_excel)
        new_file_excel = self.file_excel.parent / self.name_file
        to_excel(images_parameters, self.columns_title, new_file_excel)

        for massage in logs:
            self.log(f"Не удалось перенести {massage} из-за нехватки вводных данных")

        self.log(show_info_script_completed())

    def log(self, message):
        self.text_log.insert('end', message + '\n')
        self.text_log.see('end')

    def get_excel(self):
        self.file_excel = Path(filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")]))
        self.entry_get_file.insert(tk.END, self.file_excel)


class TabOne:
    def __init__(self, tab: tk.CTkFrame, text_log: tk.CTkTextbox):
        self.tab = tab
        self.COLUMN_TITLE = [field.description for _, field in ImageParameters.model_fields.items()]
        self.name_file = "Промежуточная_таблица_1.xlsx"
        self.text_log = text_log

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

        self.folder_selected: Path | None = None

    def log(self, message):
        self.text_log.insert('end', message + '\n')
        self.text_log.see('end')

    def run_script(self):
        if not self.folder_selected or not self.folder_selected.is_dir():
            return show_warning_no_directory()
        self.log("Скрипт запущен!")
        logs = []
        sub_folders, images_parameters, article, logs = run_rename_files_and_dirs(
            self.folder_selected,
            settings.article,
            self.folder_selected.name,
            logs,
        )
        rename_path(images_parameters, self.folder_selected)
        new_file_excel = self.folder_selected.parent / self.name_file

        to_excel(images_parameters, self.COLUMN_TITLE, new_file_excel)

        for log in logs:
            self.log(log)

        self.log(show_info_script_completed())

    def get_directory(self):
        self.folder_selected = Path(filedialog.askdirectory())
        self.entry_choice_directory.insert(tk.END, self.folder_selected)


class TabTwo(BaseTab):
    def __init__(self, tab: tk.CTkFrame, text_log: tk.CTkTextbox):
        self.tab = tab
        name_script = "Скрипт 2. Распределение по папкам с соответствующими размерами."
        self.name_file = "Промежуточная_таблица_2.xlsx"
        self.text_log = text_log
        super().__init__(
            tab=self.tab,
            base_model=DistributedPictures,
            name_script=name_script,
            name_file=self.name_file,
            text_log=self.text_log,
        )

    def script(self, file_excel: Path):
        return get_unique_values(file_excel)


class TabThree:
    def __init__(self, tab: tk.CTkFrame, text_log: tk.CTkTextbox):
        self.tab = tab
        name_script = "Скрипт 3. Распределение по папкам после фотошопа."
        self.name_file = "Промежуточная_таблица_3.xlsx"
        self.COLUMN_TITLE = [field.description for _, field in DistributedPictures.model_fields.items()]
        self.file_excel = None
        self.text_log = text_log

        # Создание метки наименования
        self.label = tk.CTkLabel(master=self.tab, text=name_script)
        self.label.grid(row=0, columnspan=2, padx=20, pady=10)

        # Создание метки для выбора исходной папки
        self.text_choice_directory = tk.CTkLabel(self.tab, text="Исходная папка с изображениями:")
        self.text_choice_directory.grid(row=1, columnspan=2, padx=20, pady=10)

        # Создание окна выбора исходной папки
        self.entry_choice_directory = tk.CTkEntry(self.tab, width=500)
        self.entry_choice_directory.grid(row=2, columnspan=2, padx=20, pady=10)

        # Создание кнопки запуска скрипта
        self.button_get_directory = tk.CTkButton(self.tab, text="Выбор папки", command=self.get_directory)
        self.button_get_directory.grid(row=3, column=1, padx=20, pady=10)

        # Создание метки для выбора исходной папки
        self.text_choice_file = tk.CTkLabel(self.tab, text="Исходный файл excel:")
        self.text_choice_file.grid(row=4, columnspan=2, padx=20, pady=10)

        # Создание окна выбора исходной папки
        self.entry_get_file = tk.CTkEntry(self.tab, width=500)
        self.entry_get_file.grid(row=5, columnspan=2, padx=20, pady=10)

        # Создание кнопки запуска скрипта
        self.button_choice_directory = tk.CTkButton(self.tab, text="Запустить", command=self.run_script)
        self.button_choice_directory.grid(row=6, column=0, padx=20, pady=10)

        # Создание кнопки запуска скрипта
        self.button_get_file = tk.CTkButton(self.tab, text="Выбор файла", command=self.get_excel)
        self.button_get_file.grid(row=6, column=1, padx=20, pady=10)

        self.folder_selected: Path | None = None

    def log(self, message):
        self.text_log.insert('end', message + '\n')
        self.text_log.see('end')

    def run_script(self):
        if not self.folder_selected or not self.folder_selected.is_dir():
            return show_warning_no_directory()

        if not self.file_excel or not self.file_excel.is_file():
            return show_warning_no_directory()

        self.log("Скрипт запущен!")

        images_parameters, logs = run_distribution_files_in_base_path(
            file_excel=self.file_excel,
            base_path=self.folder_selected,
        )

        new_file_excel = self.file_excel.parent / self.name_file
        to_excel(images_parameters, self.COLUMN_TITLE, new_file_excel)

        for log in logs:
            self.log(log)

        self.log(show_info_script_completed())

    def get_directory(self):
        self.folder_selected = Path(filedialog.askdirectory())
        self.entry_choice_directory.insert(tk.END, self.folder_selected)

    def get_excel(self):
        self.file_excel = Path(filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")]))
        self.entry_get_file.insert(tk.END, self.file_excel)


class TabFour(BaseTab):
    def __init__(self, tab: tk.CTkFrame, text_log: tk.CTkTextbox):
        self.tab = tab
        name_script = "Скрипт 4. Составление таблицы финальной таблицы без вариаций."
        self.name_file = "Промежуточная_таблица_4.xlsx"
        self.text_log = text_log
        super().__init__(
            tab=self.tab,
            base_model=FinalTable,
            name_script=name_script,
            name_file=self.name_file,
            text_log=self.text_log
        )

    def script(self, file_excel: Path):
        return run_final_table_without_variations(file_excel)


class TabFive(BaseTab):
    def __init__(self, tab: tk.CTkFrame, text_log: tk.CTkTextbox):
        self.tab = tab
        name_script = "Скрипт 5. Составление таблицы финальной таблицы c вариациями."
        self.name_file = "Промежуточная_таблица_5.xlsx"
        self.text_log = text_log
        super().__init__(
            tab=self.tab,
            base_model=FinalTable,
            name_script=name_script,
            name_file=self.name_file,
            text_log=self.text_log,
        )

    def script(self, file_excel: Path):
        return run_final_table_with_variations(file_excel)


class TabSix:
    def __init__(self, tab: tk.CTkFrame, text_log: tk.CTkTextbox):
        self.tab = tab
        self.COLUMN_TITLE = [field.description for _, field in RepeatImages.model_fields.items()]
        self.name_file = "Промежуточная_таблица_6.xlsx"
        self.text_log = text_log

        # Создание метки наименования
        self.label = tk.CTkLabel(master=self.tab, text="Скрипт 6. Категории с одинаковыми изображениями.")
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

        self.folder_selected: Path | None = None

    def log(self, message):
        self.text_log.insert('end', message + '\n')
        self.text_log.see('end')

    def run_script(self):
        if not self.folder_selected or not self.folder_selected.is_dir():
            return show_warning_no_directory()
        self.log("Скрипт запущен!")
        logs = []
        sub_folders, images_parameters = run_repeat_images(
            self.folder_selected,
            self.folder_selected.name,
        )
        images = [value for value in images_parameters.values()]
        new_file_excel = self.folder_selected.parent / self.name_file
        to_excel(images, self.COLUMN_TITLE, new_file_excel)

        for log in logs:
            self.log(log)

        self.log(show_info_script_completed())

    def get_directory(self):
        self.folder_selected = Path(filedialog.askdirectory())
        self.entry_choice_directory.insert(tk.END, self.folder_selected)


class TabSettings:
    def __init__(self, tab: tk.CTkFrame, text_log: tk.CTkTextbox):
        self.tab = tab
        self.text_log = text_log

        # Создание метки "Настройки"
        self.label = tk.CTkLabel(master=self.tab, text="Настройки.")
        self.label.grid(row=0, columnspan=3, padx=20, pady=10)

        # Создание метки для изменения артикула
        self.text_update_article = tk.CTkLabel(self.tab, text="Артикул:")
        self.text_update_article.grid(row=1, column=0, padx=20, pady=10)

        # Создание окна для изменения артикула
        self.entry_update_article = tk.CTkEntry(self.tab, width=500)
        self.entry_update_article.insert(tk.END, settings.article)
        self.entry_update_article.grid(row=1, column=1, columnspan=2, padx=20, pady=10)

        # Создание метки для изменения ссылки
        self.text_update_url = tk.CTkLabel(self.tab, text="Ссылка:")
        self.text_update_url.grid(row=2, column=0, padx=20, pady=10)

        # Создание окна для изменения ссылки
        self.entry_update_url = tk.CTkEntry(self.tab, width=500)
        self.entry_update_url.insert(tk.END, settings.url)
        self.entry_update_url.grid(row=2, column=1, columnspan=2, padx=20, pady=10)

        # Создание метки для изменения файла вариаций
        self.text_update_variable = tk.CTkLabel(self.tab, text="Файл вариаций:")
        self.text_update_variable.grid(row=3, column=0, padx=20, pady=10)

        # Создание окна для изменения файла вариаций
        self.entry_update_variable = tk.CTkEntry(self.tab, width=500)
        self.entry_update_variable.insert(tk.END, settings.variable)
        self.entry_update_variable.grid(row=3, column=1, columnspan=2, padx=20, pady=10)

        # Создание метки для перемешивания ссылок
        self.text_random_links = tk.CTkLabel(self.tab, text="Перемешать ссылки:")
        self.text_random_links.grid(row=4, column=0, padx=20, pady=10)

        # Создание метки для изменения файла вариаций
        value = "on" if settings.is_random_links else "off"
        self.is_random_links = settings.is_random_links
        self.check_var = tk.StringVar(value=value)
        self.random_links_box = tk.CTkCheckBox(
            self.tab, text="", command=self.checkbox_event, variable=self.check_var, onvalue="on", offvalue="off"
        )
        self.random_links_box.grid(row=4, column=1, padx=20, pady=10)

        # Создание кнопки для изменения настроек
        self.button_choice_directory = tk.CTkButton(self.tab, text="Изменить", command=self.update_settings)
        self.button_choice_directory.grid(row=5, column=1, padx=20, pady=10)

    def checkbox_event(self):
        if self.check_var.get() == 'on':
            self.is_random_links = True
            settings.is_random_links = True
        else:
            self.is_random_links = False
            settings.is_random_links = False

    def update_settings(self):
        article = self.entry_update_article.get()
        url = self.entry_update_url.get()
        variable = self.entry_update_variable.get()
        settings.update_article_settings(article)
        settings.update_url_settings(url)
        settings.update_variable_settings(variable)
        settings.update_is_random_links_settings(self.is_random_links)
        self.log(message="Настройки изменены!")

    def log(self, message):
        self.text_log.insert('end', message + '\n')
        self.text_log.see('end')


class MyTabView(tk.CTkTabview):
    def __init__(self, master, text_log, **kwargs):
        self.text_log = text_log
        super().__init__(master, **kwargs)

        # create tabs
        self.add("1")
        self.add("2")
        self.add("3")
        self.add("4")
        self.add("5")
        self.add("6")
        self.add("7")

        TabOne(self.tab("1"), self.text_log)
        TabTwo(self.tab("2"), self.text_log)
        TabThree(self.tab("3"), self.text_log)
        TabFour(self.tab("4"), self.text_log)
        TabFive(self.tab("5"), self.text_log)
        TabSix(self.tab("6"), self.text_log)
        TabSettings(self.tab("7"), self.text_log)


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ART PROJECT")

        label_1 = tk.CTkLabel(master=self, text="1. Переименование папок и файлов.")
        label_1.grid(row=0, column=0, ipadx=50, padx=1, pady=1, sticky="w")

        label_2 = tk.CTkLabel(master=self, text="2. Распределение по папкам с соответствующими размерами.")
        label_2.grid(row=1, column=0, ipadx=50, padx=1, pady=1, sticky="w")

        label_3 = tk.CTkLabel(master=self, text="3. Распределение по папкам после фотошопа.")
        label_3.grid(row=2, column=0, ipadx=50, padx=1, pady=1, sticky="w")

        label_4 = tk.CTkLabel(master=self, text="4. Составление таблицы финальной таблицы без вариаций.")
        label_4.grid(row=3, column=0, ipadx=50, padx=1, pady=1, sticky="w")

        label_5 = tk.CTkLabel(master=self, text="5. Составление таблицы финальной таблицы c вариациями.")
        label_5.grid(row=4, column=0, ipadx=50, padx=1, pady=1, sticky="w")

        label_6 = tk.CTkLabel(master=self, text="6. Категории с одинаковыми изображениями.")
        label_6.grid(row=5, column=0, ipadx=50, padx=1, pady=1, sticky="w")

        label_7 = tk.CTkLabel(master=self, text="7. Настройки.")
        label_7.grid(row=6, column=0, ipadx=50, padx=1, pady=1, sticky="w")

        # Создание окна лога
        self.text_log = tk.CTkTextbox(self, width=550)
        self.text_log.grid(row=8, column=0, columnspan=3, padx=20, pady=10)

        self.tab_view = MyTabView(master=self, text_log=self.text_log)
        self.tab_view.grid(row=7, column=0, padx=20, pady=20)

