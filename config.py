from dotenv import load_dotenv, find_dotenv
import os

# Find .env file
load_dotenv(find_dotenv())

API_TOKEN = os.getenv('API_TOKEN')