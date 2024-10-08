from fastapi import APIRouter, HTTPException
from app.models import Car
from app.controllers import get_cars, get_car_by_id, delete_car_by_id, create_car

car_router = APIRouter()


# ? GET ALL CARS
@car_router.get("/api/cars", response_model=list[Car])
async def get_cars_route():
    return await get_cars()


# ? GET CAR BY ID
@car_router.get("/api/cars/{car_id}", response_model=Car)
async def get_car_by_id_route(car_id: str):
    car = await get_car_by_id(car_id)
    if car:
        return car
    raise HTTPException(status_code=404, detail="Car not foundd with " + car_id)


# ? DELETE CAR BY ID
@car_router.delete("/api/cars/{car_id}")
async def delete_car_by_id_route(car_id: str):
    success = await delete_car_by_id(car_id)
    if success:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found  with id" + car_id)


# ? CREATE CAR
@car_router.post("/api/cars", response_model=Car)
async def create_car_route(car: Car):
    return await create_car(car.model_dump())
