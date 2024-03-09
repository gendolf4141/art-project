#!/bin/bash

# Устанавливаем необходимые зависимости (если еще не установлены)
pip install virtualenv
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt

# Переходим в директорию проекта
#cd /path/to/customtkinter

# Собираем проект с помощью PyInstaller
#pyinstaller --onefile --noconsole main.py
#pyinstaller --noconfirm --onedir --windowed --add-data "<CustomTkinter Location>/customtkinter;customtkinter/"  "main.py"
pyinstaller -F --onefile --noconsole main.py --collect-all customtkinter
# Перемещаем .exe файл из директории dist в желаемую директорию
#mv dist/main.exe ./art-project.exe

# Очищаем временные файлы, созданные PyInstaller
#rm -rf build dist __pycache__ *.spec
