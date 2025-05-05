import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

load_dotenv()


MONGODB_URL = os.getenv("MONGODB_URI")
DB_NAME = "cars_database_python"
COLLECTION_NAME = "cars"

client = AsyncIOMotorClient(MONGODB_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

async def seed_data():
    seedCarsData = [
        {"name": "Toyota Corolla", "price": 20000},
        {"name": "Honda Civic", "price": 22000},
        {"name": "Ford Mustang", "price": 30000},
        {"name": "Chevrolet Camaro", "price": 32000},
        {"name": "BMW 3 Series", "price": 35000},
        {"name": "Mercedes-Benz C-Class", "price": 40000},
        {"name": "Audi A4", "price": 37000},
        {"name": "Tesla Model 3", "price": 45000},
        {"name": "Mazda CX-5", "price": 28000},
        {"name": "Subaru Outback", "price": 31000},
    ]
    removed = await collection.delete_many({})
    print(f"{removed.deleted_count} cars removed from the database.")
    result = await collection.insert_many(seedCarsData)
    print(f"{len(result.inserted_ids)} cars inserted into the database.")

if __name__ == "__main__":
    asyncio.run(seed_data())
