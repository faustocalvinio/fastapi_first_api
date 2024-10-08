from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import asyncio

# Database configuration
MONGODB_URL = "mongodb://admin:admin_password@127.0.0.1:27017/"
DB_NAME = "cars_database"
COLLECTION_NAME = "cars"

# Initialize MongoDB connection
client = AsyncIOMotorClient(MONGODB_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Define the Car model
class Car(BaseModel):
    name: str
    price: int

# Seed data
async def seed_data():
    cars = [
        {"name": "Toyota Corolla", "price": 20000},
        {"name": "Honda Civic", "price": 22000},
        {"name": "Ford Mustang", "price": 30000},
        {"name": "Chevrolet Camaro", "price": 32000},
        {"name": "BMW 3 Series", "price": 35000},
        {"name": "Mercedes-Benz C-Class", "price": 40000},
        {"name": "Audi A4", "price": 37000},
        {"name": "Tesla Model 3", "price": 45000},
        {"name": "Mazda CX-5", "price": 28000},
        {"name": "Subaru Outback", "price": 31000}
    ]

    # Insert seed data into the collection
    result = await collection.insert_many(cars)
    print(f"{len(result.inserted_ids)} cars inserted into the database.")

# Main function to run the seed
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(seed_data())
