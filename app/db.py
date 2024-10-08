from motor.motor_asyncio import AsyncIOMotorClient

#! DB CONFIG
MONGODB_URL = "mongodb+srv://fausto:NgbO3lSX8hgvpONx@cluster0.puxrytr.mongodb.net/"
DB_NAME = "cars_database"
COLLECTION_NAME = "cars"

#! INIT MONGO
client = AsyncIOMotorClient(MONGODB_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
