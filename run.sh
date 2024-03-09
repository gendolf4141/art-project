#!/bin/bash

# Устанавливаем необходимые зависимости (если еще не установлены)
pip install pyinstaller

# Переходим в директорию проекта
#cd /path/to/customtkinter

# Собираем проект с помощью PyInstaller
pyinstaller --onefile --noconsole main.py

# Перемещаем .exe файл из директории dist в желаемую директорию
mv dist/main.exe ./art-project.exe

# Очищаем временные файлы, созданные PyInstaller
#rm -rf build dist __pycache__ *.spec
