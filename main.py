from fastapi import FastAPI
import modals
import database

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Hello Mongo"}

@app.get("/all")
def get_all():
    data = database.all()
    return {"data" : data}

@app.post("/create")
def create(data :modals.Todo):
    id = database.create(data)
    return {"inserted":True, "inserted_id":id}

#@app.get("/get/{name}")
@app.get("/get")
def get_one(name :str):
    data = database.get_one(name)
    return {"data" : data}

@app.delete("/delete")
def delete(name:str):
    data = database.delete(name)
    return {"deleted":True, "deleted_count":data}

@app.put("/update")
def update(data:modals.Todo):
    data = database.update(data)
    return {"updated":True, "updated_count": data}
    