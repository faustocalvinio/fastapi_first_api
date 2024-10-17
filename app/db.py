import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

#! DB CONFIG
# MONGODB_URL = os.getenv('MONGODB_URI')
MONGODB_URL = os.getenv('MONGODB_URI')
DB_NAME = "cars_database_python"
COLLECTION_NAME = "cars"

#! INIT MONGO
print(MONGODB_URL)
client = AsyncIOMotorClient(MONGODB_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
