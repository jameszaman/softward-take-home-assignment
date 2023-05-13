from dotenv import load_dotenv
from os import environ
from pathlib import Path

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# MongoDB
MONGO_URI = environ.get('MONGO_URI', 'mongodb://localhost:27017')
MONGO_DB_NAME = environ.get('MONGO_DB_NAME', 'softward')

# FastAPI
API_PREFIX = environ.get('API_PREFIX', '/api/v1')
API_KEY = environ.get('API_KEY')