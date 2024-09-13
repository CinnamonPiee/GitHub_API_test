import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Получаем необходимые данные из окружения
GITHUB_API_URL = "https://api.github.com"
USERNAME = os.getenv('GITHUB_USERNAME')
TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')


def create_repository():
    """Создание нового публичного репозитория на GitHub"""
    url = f"{GITHUB_API_URL}/user/repos"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": REPO_NAME,
        "description": "Repository created for testing GitHub API",
        "private": False
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Repository '{REPO_NAME}' created successfully.")
    else:
        print(f"Failed to create repository: {response.status_code}, {response.text}")
    return response.status_code


def check_repository_exists():
    """Проверка, существует ли репозиторий"""
    url = f"{GITHUB_API_URL}/repos/{USERNAME}/{REPO_NAME}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Repository '{REPO_NAME}' exists.")
    else:
        print(f"Repository '{REPO_NAME}' not found: {response.status_code}, {response.text}")
    return response.status_code


def delete_repository():
    """Удаление репозитория"""
    url = f"{GITHUB_API_URL}/repos/{USERNAME}/{REPO_NAME}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{REPO_NAME}' deleted successfully.")
    else:
        print(f"Failed to delete repository: {response.status_code}, {response.text}")
    return response.status_code


def run_test():
    """Запуск теста создания, проверки и удаления репозитория"""
    print("Starting GitHub API test...")

    create_status = create_repository()
    if create_status != 201:
        print("Test failed: Could not create repository.")
        return

    check_status = check_repository_exists()
    if check_status != 200:
        print("Test failed: Repository not found after creation.")
        return

    delete_status = delete_repository()
    if delete_status != 204:
        print("Test failed: Could not delete repository.")
        return

    check_status_after_delete = check_repository_exists()
    if check_status_after_delete == 404:
        print("Test passed: Repository deleted successfully.")
    else:
        print("Test failed: Repository still exists after deletion.")


if __name__ == "__main__":
    run_test()
