import tkinter.messagebox as mb


def show_warning_no_directory():
    msg = "Путь не выбран или не является папкой!"
    mb.showwarning("Предупреждение", msg)


def show_warning_no_article() -> str:
    msg = "Необходимо задать значение по умолчанию для ARTICLE в файле .env!"
    mb.showwarning("Предупреждение", msg)
    return msg


def show_warning_no__is_random_links() -> str:
    msg = "Необходимо задать значение по умолчанию для IS_RANDOM_LINKS в файле .env!"
    mb.showwarning("Предупреждение", msg)
    return msg


def show_warning_no_variable() -> str:
    msg = "Необходимо задать значение по умолчанию для VARIABLE в файле .env!"
    mb.showwarning("Предупреждение", msg)
    return msg


def show_warning_no_url() -> str:
    msg = "Необходимо задать значение по умолчанию для URL в файле .env!"
    mb.showwarning("Предупреждение", msg)
    return msg


def show_info_script_completed() -> str:
    msg = "Выполнение скрипта завершено!"
    mb.showinfo("Информация", msg)
    return msg
