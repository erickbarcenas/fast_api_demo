from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

users = {
    1: {"id": 1, "name": "Erick", "age": 20},
    2: {"id": 2, "name": "Ivan", "age": 20}
}


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/")
def login(request: Request):
    print(Request)



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
