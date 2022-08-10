from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return 'hello'

# @app.get("/data")
# def root():
#     return {'hello' : 1234}

# @app.get("/res")
# def root():
#     return FileResponse("index.html")

# from pydantic import BaseModel

# class Model(BaseModel):
#     name : str
#     phone : int
    
    
# @app.post("/send")
# def root(data : Model):
#     print(data)
#     return "Send Complete"

@app.get("/item/{item_id}")
async def read_item(item_id):
    return {"item_id" : item_id}

# @app.get("/items/{item_id}") # 타입이 있는 매개변수
# async def read_item(item_id: int):
#     return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 2):
#     return fake_items_db[skip : skip + limit]

from typing import Union

# @app.get("/items/{item_id}")
# async def read_item(item_id: str,  q : Union[str, None] = None):
#     if q:
#         return {"item_id" : item_id, "q" : q}
#     return {"item_id" : item_id}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

# needy, 필수적인 str
# skip, 기본값이 0인 int
# limit, 선택적인 int
#파라미터 지정 : http://127.0.0.1:8000/items/foo-item?needy=sooooneedy&skip=5&limit=4