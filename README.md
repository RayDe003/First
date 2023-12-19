# Установка

1. Клонируйте репозиторий
```bash
   git clone https://github.com/RayDe003/First
```

2. Перейдите в директорию проекта
```bash
   cd myblog
```
3. Утсановите зависимости
```bash
   pip install django 
   pip install Pillow
```
# Запуск
1. Выполните миграции
   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```

2. Запустите сервер
   ```bash
     python manage.py runserver
   ```
3. Вход в панель администратора
```bash
По адресу: http://localhost:8000/admin/
