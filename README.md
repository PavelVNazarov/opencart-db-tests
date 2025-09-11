# OpenCart DB Testing Framework

Фреймворк для автоматизированного тестирования базы данных OpenCart с использованием Python, PyMySQL и pytest.

## 🎯 Цель

Научиться использовать Python для выполнения SQL-запросов к базе данных MariaDB/MySQL, эмулируя реальные сценарии работы интернет-магазина OpenCart:
- Создание, обновление и удаление клиентов
- Работа с товарами и категориями
- Проверка негативных сценариев

## 🧰 Технологии

- **Python 3.7+**
- **PyMySQL** — драйвер для подключения к MySQL/MariaDB
- **pytest** — фреймворк для написания и запуска тестов
- **MariaDB/MySQL** — система управления базами данных

## 📦 Установка зависимостей

pip install pytest PyMySQL
Для аутентификации caching_sha2_password (актуально для MySQL 8+):

pip install PyMySQL[rsa]
🔧 Настройка базы данных
Установите и запустите MariaDB или XAMPP.
Создайте базу данных:

CREATE DATABASE opencart_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
Создайте таблицу oc_customer (или установите OpenCart).
Пример создания таблицы:

USE opencart_db;

CREATE TABLE oc_customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(32) NOT NULL,
    lastname VARCHAR(32) NOT NULL,
    email VARCHAR(96) NOT NULL,
    telephone VARCHAR(32) NOT NULL,
    password VARCHAR(255) NOT NULL,
    salt VARCHAR(9),
    status TINYINT(1) DEFAULT 1,
    date_added DATETIME NOT NULL
);
⚙️ Запуск тестов
Запустите тесты с параметрами подключения к БД:

pytest tests/test_customer.py -v \
  --host=localhost \
  --port=3306 \
  --database=opencart_db \
  --user=root \
  --password=your_password
🧪 Проведённые тесты
test_create_customer
Создаёт нового клиента и проверяет его наличие в базе данных
test_update_existing_customer
Обновляет данные существующего клиента
test_update_nonexistent_customer
Негативный тест: обновление несуществующего клиента
test_delete_existing_customer
Удаляет клиента и проверяет, исчез ли он из базы данных
test_delete_nonexistent_customer
Отрицательный тест: удаление несуществующего клиента

Также добавлены расширенные тесты:

Работа с товарами (oc_product)
Работа с категориями (oc_category)
Привязка товара к категории
📂 Структура проекта

opencart_db_framework/

├── conftest.py               # Фикстуры и параметры pytest

├── lib/

│   └── db.py                 # Функции для работы с БД

├── tests/

│   ├── test_customer.py      # Тесты для клиентов

│   └── test_product.py       # Тесты для товаров и категорий

├── .gitignore                # Игнорируемые файлы

└── README.md                 # Документация проекта

🛠️ Автор
Павел Назаров
GitHub: @PavelVNazarov
проверьте другую ветку
