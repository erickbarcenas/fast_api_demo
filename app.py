from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

users = {
    1: {"id": 1, "name": "Erick", "age": 20},
    2: {"id": 2, "name": "Ivan", "age": 20}
}


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/user/{user_id}")
def user(user_id: int):
    return {"id": users[user_id]["id"]}


'''
@app.get("/suma/{num1}&{num2}")
def add(num1: float, num2: float):
    return {"suma": num1 + num2}
'''
