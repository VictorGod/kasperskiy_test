# kasperskiy_test

Описание вашего проекта.

## Описание

Этот проект автоматизирует выполнение трех тестов с использованием Page Object паттерна и библиотек python 3.6+, pytest, selenium (или playwright), chromedriver.

## Структура проекта

```plaintext
|-- framework/
|   |-- pages/
|   |   |-- support_page.py
|   |   |-- industrial_cybersecurity_page.py
|-- tests/
|   |-- test_support_page.py
|   |-- test_check_sensor_ram_v40.py
|   |-- test_check_sensor_ram_v30.py
|   |-- test_check_sensor_ram_v40_rus.py
|-- requirements.txt
|-- README.md
```

- **framework/**: Содержит Page Object модели для ваших страниц.
- **tests/**: Содержит ваши автоматизированные тесты.
- **requirements.txt**: Файл, содержащий библиотеки и их версии, необходимые для запуска проекта.
- **README.md**: Файл с описанием проекта и инструкциями по запуску.

## Установка зависимостей

Для установки зависимостей выполните следующую команду:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Для запуска тестов используйте команду:

```bash
pytest tests/
```

## Описание тестов

### `test_check_sensor_ram_v40`

1. Открывает https://support.kaspersky.com/help/
2. Находит на странице "Industrial CyberSecurity for Networks"
3. Открывает версию 4.0
4. В справке открывает "About Kaspersky Industrial CyberSecurity for Networks"
5. Открывает "Hardware and software requirements"
6. Находит текст "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer"
7. Assert, что текст соответствует "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer"

### `test_check_sensor_ram_v30`

1. Открывает https://support.kaspersky.com/help/
2. Находит на странице "Industrial CyberSecurity for Networks"
3. Открывает версию 3.0
4. В справке открывает "About Kaspersky Industrial CyberSecurity for Networks"
5. Открывает "Hardware and software requirements"
6. Находит текст "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer."
7. Assert, что текст соответствует "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer."

### `test_check_sensor_ram_v40_rus`

1. Открывает https://support.kaspersky.com/help/
2. Находит на странице "Industrial CyberSecurity for Networks"
3. Открывает версию 4.0
4. В справке открывает "О Kaspersky Industrial CyberSecurity for Networks"
5. Открывает "Аппаратные и программные требования"
6. Находит текст "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;"
7. Assert, что текст соответствует "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;"


