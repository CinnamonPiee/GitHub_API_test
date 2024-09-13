# GitHub API E2E Test

## Описание
Этот проект содержит автоматический тест для работы с GitHub API. Скрипт создает новый репозиторий, проверяет его наличие и затем удаляет репозиторий.

## Установка
1. Клонируйте репозиторий

    ```bash
    git clone https://github.com/CinnamonPiee/GitHub_API_test
    ```

2. Создайте и активируйте виртуальное окружение

   - Windows
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

   - Linux and MacOS
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Установите зависимости

    ```bash
    pip install -r requirements.txt
    ```
   
4. Создайте файл .env по примеру файла .env.template и добавьте свои данные GitHub:

## Запуск
Для запуска теста выполните следующую команду:
- Windows
    ```bash
    python test_api.py 
    ```

- Linux and MacOS
    ```bash
    python3 test_api.py 
    ```