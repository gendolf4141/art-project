#!/bin/bash

# Устанавливаем необходимые зависимости (если еще не установлены)
C:/Users/da_et/AppData/Local/Programs/Python/Python312/python.exe -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

# Собираем проект с помощью PyInstaller
pyinstaller -F --onefile --noconsole main.py --collect-all customtkinter

# Перемещаем .exe файл из директории dist в желаемую директорию
mv dist/main.exe ./art-project.exe

# Очищаем временные файлы, созданные PyInstaller
rm -rf build dist __pycache__ *.spec
