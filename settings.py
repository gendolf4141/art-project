from dotenv import find_dotenv, load_dotenv, set_key
from messages import show_warning_no_article, show_warning_no_url, show_warning_no_variable
import os

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

article = os.getenv("ARTICLE")
url = os.getenv("URL")
variable = os.getenv("VARIABLE")

if not article:
    show_warning_no_article()
    exit()
else:
    article = int(article)

if not url:
    show_warning_no_url()
    exit()


if not variable:
    show_warning_no_variable()
    exit()
else:
    variable = variable


def update_article_settings(article):
    """Обновляет значение артикула в файле .env"""
    os.environ["ARTICLE"] = article
    set_key(dotenv_file, "ARTICLE", os.environ["ARTICLE"])


def update_url_settings(url: str):
    """Обновляет значение ссылки в файле .env"""
    os.environ["URL"] = url
    set_key(dotenv_file, "URL", os.environ["URL"])


def update_variable_settings(variable: str):
    """Обновляет значение пути файла вариаций в файле .env"""
    os.environ["VARIABLE"] = variable
    set_key(dotenv_file, "VARIABLE", os.environ["VARIABLE"])