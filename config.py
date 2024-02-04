from dotenv import load_dotenv, find_dotenv
import os

# Find .env file
load_dotenv(find_dotenv())

# Получаем значение API_TOKEN
API_TOKEN = os.getenv('API_TOKEN')

# Если .env файл отсутствует, используем переменную окружения API_TOKEN
if API_TOKEN is None:
    API_TOKEN = os.environ.get('API_TOKEN')

if API_TOKEN is None:
    raise ValueError("API_TOKEN is not set. Create a .env file or set it as an environment variable.")
