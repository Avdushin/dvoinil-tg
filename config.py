from dotenv import load_dotenv, find_dotenv
import os

# Find .env file
load_dotenv(find_dotenv())

# API_TOKEN = os.getenv('API_TOKEN')

API_TOKEN = "6911174045:AAE3j4qZJGtgx1PIahWaOvW07e8S9rDQG_c"

# # Если .env файл отсутствует, используем переменную окружения API_TOKEN
# if API_TOKEN is None:
#     API_TOKEN = os.environ.get('API_TOKEN')

# if API_TOKEN is None:
#     # For test production
#     API_TOKEN = "6911174045:AAE3j4qZJGtgx1PIahWaOvW07e8S9rDQG_c"
