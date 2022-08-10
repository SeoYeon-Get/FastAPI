# from fastapi import FastAPI
# from pydantic import BaseModel
# import requests

# app = FastAPI()

# db = []

# class City(BaseModel):
#     name : str
#     timezone : str
    
# @app.get("/")
# def root():
#     return {"Hello" : "Seoul!"}

# @app.get('/cities')
# def get_cities():
#     results = []
#     for city in db:
#         strs = f"http://worldtimeapi.org/timezone/{city['timezone']}"
#         r = requests.get(strs)
#         cur_ime = r.json()['datetime']
#         results.append({'name' : city['name'], 'timezone':city['timezone'], 'current_time':cur_time})
        
# @app.get('/cities/{city_id}')
# def get_city(city_id: int):
    
#     city = db[city_id-1]
    
#     strs = f"http://worldtimeapi.org/timezone/{city['timezone']}"
#     r = requests.get(strs)
#     cur_time = r.json()['datetime']
    
#     return {'name':city['name'], 'timezone':city['timezone'], 'cur_time':cur_time}


# @app.post('/cities')
# def create_city(city : City):
#     db.append(city.dict())
#     return db[-1]

from typing import Union

from fastapi import FastAPI, Form , Path, Request
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
#     q: Union[str, None] = None,
#     item: Union[Item, None] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results


# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# def fake_password_hasher(raw_password: str):
#     return "supersecret" + raw_password


# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print("User saved! ..not really")
#     return user_in_db


# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved@app.get("/order_food", response_class=HTMLResponse)

from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory = "templates")

@app.get("/order_food", response_class = HTMLResponse)
def order_food(request: Request):
    return templates.TemplateResponse("order_food.html", {"request": request})

@app.post("/submit")
def submit_food(food:str = Form(...)):
    s = f"{food} 주문완료"
    print(s)
    return s