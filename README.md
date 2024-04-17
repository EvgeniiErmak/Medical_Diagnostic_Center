# Medical Diagnostic Center

**Medical Diagnostic Center** — это веб-платформа для управления медицинскими услугами, которая позволяет пациентам записываться на прием к специалистам, просматривать медицинские ресурсы и получать онлайн-консультации.

## Структура проекта

Проект включает следующие компоненты:

- **Medical_Diagnostic_Center**: основная директория проекта, содержит конфигурации Django и ASGI/WSGI приложения.
- **appointments**: модуль для управления записями на приемы.
- **authentication**: модуль для аутентификации и управления пользователями.
- **clinic**: информация о клинике и специалистах.
- **educational_resources**: образовательные материалы и ресурсы для пациентов.
- **feedback**: отзывы и FAQ.
- **online_consultations**: система онлайн-консультаций через WebRTC.
- **templates**: глобальные шаблоны для проекта.

## Технологии

- **Django** 5.0.4: основной фреймворк для веб-разработки.
- **PostgreSQL**: основная система управления базами данных.
- **Channels**: для асинхронной работы и Websockets.
- **Django REST framework** и **drf-yasg**: для создания API и его документации.
- **Bootstrap 4**: для стилизации фронтенда.

## Настройка проекта

### Зависимости

Установите все зависимости проекта через Poetry:

```bash
poetry install
```

### Конфигурация

Конфигурационные параметры проекта находятся в файле `settings.py`. Вам нужно настроить доступ к базе данных, почтовому серверу и другие параметры, используя переменные окружения. Пример файла `.env`:

```plaintext
DEBUG=True
SECRET_KEY='your_secret_key'
DB_NAME='dbname'
DB_USER='dbuser'
DB_PASSWORD='dbpassword'
DB_HOST='localhost'
DB_PORT='5432'
EMAIL_HOST_USER='your-email@gmail.com'
EMAIL_HOST_PASSWORD='your-email-password'
REDIS_HOST='localhost'
REDIS_PORT=6379
```

### База данных

Выполните миграции для создания структуры базы данных:

```bash
poetry run python manage.py migrate
```

### Запуск проекта

Запустите сервер разработки:

```bash
poetry run python manage.py runserver
```

## Тестирование

Запустите тесты, чтобы проверить корректность всех компонентов системы:

```bash
poetry run python manage.py test
```

## Документация API

Документацию API можно просмотреть, перейдя по адресу `/swagger/` после запуска проекта.

## Административная панель

Для доступа к административной панели Django используйте URL `/admin/`. Предварительно создайте суперпользователя:

```bash
poetry run python manage.py createsuperuser
```

---
