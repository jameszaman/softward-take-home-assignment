from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from config import MONGO_URI, MONGO_DB_NAME


client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=5000)
try:
    client.admin.command('ping')
    print('Connected to mongodb server')
except ServerSelectionTimeoutError:
    print('Error: Could not connect to MongoDB.')
    client.close()
    client = None

db = client[MONGO_DB_NAME] if client else None

