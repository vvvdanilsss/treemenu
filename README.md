# treemenu

Этот проект представляет собой простой пример реализации древовидного меню веб-приложения на фреймворке Django.

## Описание

Проект реализует следующие особенности:

1. Древовидное меню.
2. Возможность создания нескольких меню с разными названиями.
3. Редактирование меню через админку Django.
4. Активный пункт меню определяется исходя из URL текущей страницы.
5. Переход по заданным URL или URL, определенным как именованные URL в Django.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/vvvdanilsss/treemenu.git
    
   ```

2. Создайте виртуальное окружение (рекомендуется):

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Для Linux/Mac
   # или
   myenv\Scripts\activate  # Для Windows
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
    
   ```

4. Примените миграции:

   ```bash
   python manage.py migrate
    
   ```

5. Запустите локальный сервер:

   ```bash
   python manage.py runserver
    
   ```

## Использование

1. Перейдите в админку Django: `http://localhost:8000/admin/`

2. В разделе "MENUAPP" добавьте пункты меню, указав имя меню, URL (или именованный URL) и родительский элемент.

3. Добавьте пункты меню в свои HTML-шаблоны, используя тег `{% draw_menu 'menu_name' %}`, где `'menu_name'` - имя вашего меню.

Пример использования в HTML-шаблоне:

```html
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```

## Дополнительные настройки

Если вы хотите добавить новые URL или доработать структуру меню, измените файл `menuapp/urls.py` и модель `MenuItem` в `menuapp/models.py`.
