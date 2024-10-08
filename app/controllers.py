from bson import ObjectId
from app.db import collection


def car_helper(car) -> dict:
    return {
        "id": str(car["_id"]),
        "name": car["name"],
        "price": car["price"],
    }


async def get_cars():
    cars = []
    async for car in collection.find():
        cars.append(car_helper(car))
    return cars


async def get_car_by_id(car_id: str):
    car = await collection.find_one({"_id": ObjectId(car_id)})
    if car:
        return car_helper(car)
    return None


async def delete_car_by_id(car_id: str):
    delete_result = await collection.delete_one({"_id": ObjectId(car_id)})
    return delete_result.deleted_count == 1


async def create_car(car_data: dict):
    new_car = await collection.insert_one(car_data)
    created_car = await collection.find_one({"_id": new_car.inserted_id})
    return car_helper(created_car)
