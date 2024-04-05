# art-project
**Описание:**
Проект для подготовки изображений и сопутствующих файлов для загрузки на сайт https://liss-art.ru/

Для переноса проекта на локальный компьютер необходимо установить GIT(Система управления версиями)
https://git-scm.com/download/win/

Для запуска проекта необходимо установить python вирсии 3.12
https://www.python.org/downloads/release/python-3120/


Далее в консоли перейти в папку, куда запланировано копирование проекта и ввести команду:
```
git clone https://github.com/gendolf4141/art-project.git
```

Перейти в папку с проектом
```
cd art-project
```

Скопировать содержимое файла .env.example в файл .env

Запустить скрипт для сборки проекта
```
bash run.sh
```


Перезаписать данные из удаленного репозитория
```angular2html
git pull --rebase
```


Сохратить локальные изменения:
Посмотреть какие файлы были изменены:
```angular2html
git status
```

Сохранить изменения:
```angular2html
git add .
git commit -m "Комментарий"
git push
```
