Курсовая работа.

Данный проект на Python предназначен для организации рассылок посредством email.

Установка Клонируйте проект. 
Активируйте виртуальное окружение командой: poetry shell. 
Установите зависимости командой: poetry install.
Создайте Базу данных PostgreSQL, 
пропишите переменные окружения в файл .env. 
Используемые в проекте переменные окружения записаны в файле .env.sample.
Установите Redis (используется для кэширования).

Команды:

Для наполнения блога используйте команду: 
python manage.py loaddata blog.json 
Для добавления групп используйте команду: 
python manage.py loaddata groupe.json 
Для добавления пользователей используйте команду: 
python manage.py loaddata users.json







