from dotenv import find_dotenv, load_dotenv, set_key
from messages import show_warning_no_article
import os

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

article = os.getenv("ARTICLE")

if not article:
    show_warning_no_article()
    exit()
else:
    article = int(article)


def update_article_settings(article):
    """Обновляет значение артикула в файле .env"""
    os.environ["ARTICLE"] = article
    set_key(dotenv_file, "ARTICLE", os.environ["ARTICLE"])