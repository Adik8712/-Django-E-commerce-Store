## Интернет-магазин на Django

![E-commerce](https://img.shields.io/badge/E--commerce-Django-brightgreen)

Этот проект представляет собой полнофункциональное веб-приложение интернет-магазина, разработанное с использованием Django. Пользователи могут просматривать различные товары, добавлять их в корзину и осуществлять покупки. Администраторы могут управлять категориями товаров, добавлять новые продукты и отслеживать заказы.

### Особенности проекта

- **Аутентификация и авторизация**: Пользователи могут регистрироваться, аутентифицироваться и сбрасывать пароли.
- **Корзина покупок**: Пользователи могут добавлять товары в корзину, изменять количество и удалять товары перед оформлением заказа.
- **Оформление заказов**: После добавления товаров в корзину пользователи могут оформить заказ, вводя свои данные для доставки.
- **Панель администратора**: Администраторы имеют доступ к управлению категориями товаров, продуктами и заказами через административный интерфейс Django.

### Установка и запуск

1. **Клонирование репозитория**

    ```bash
    git clone https://github.com/Adik8712/Django-E-commerce-Store.git
    cd Django-E-commerce-Store/
    ```

2. **Установка и активация виртуального окружения**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # для Linux / macOS
    venv\Scripts\activate  # для Windows
    ```

3. **Установка зависимостей**

    ```bash
    pip install -r requirements.txt
    ```

4. **Применение миграций и создание суперпользователя**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

5. **Запуск сервера**

    ```bash
    python manage.py runserver
    ```

6. **Доступ к приложению**

    После запуска сервера перейдите по адресу [http://localhost:8000](http://localhost:8000) для доступа к приложению.

### Структура проекта

```
.
├── api_main
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── ...
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── main
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── ...
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── ShopDjango
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── media
│   └── ...
├── static
│   └── ...
├── templates
│   └── ...
├── venv
│   └── ...
├── README.md
└── requirements.txt
```

### Участники

- [Adik](https://github.com/Adik8712)

### Лицензия

Этот проект лицензирован по лицензии MIT - см. файл [LICENSE](LICENSE) для получения дополнительной информации.