# tech with tim fast api tutorial

from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: str = None
    price: float = None
    brand: Optional[str] = None

# @app.get("/")
# def home():
#     return {"Data": "Test"}

# @app.get("/about")
# def about():
#     return {"Data":"About"}

# inventory = {
#     1: {
#         "name": "Milk Tea",
#         "price": 3.99,
#         "brand": "Regular"
#     },
#     2: {
#         "name": "Orange Juice",
#         "price": 5.99,
#         "brand": "Sunny D"
#     },
#     3: {
#         "name": "Water",
#         "price": 0.99,
#         "brand": "Nature's Valley"
#     }
# }

# should be an actual database
inventory = {}

@app.get("/get-item/{item_id}")
# None is a required default value
def get_item(item_id: int = Path(None, description="The ID of the item you'd like to view", ge=1, le=3)):
    """Basic get endpoint, path parameters."""
    return inventory[item_id]

# @app.get("/get_item/{item_id}/{name}")
# def get_item(item_id: int):
#     return inventory[item_id]A

@app.get("/get-by-name/{name}")
def get_item(name: str=Query(None, title="Name", description="Name of the item")):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Item name not found")


# # optional query parameter
# # from typing import Optional
# * so you don't have to worry about order of required and optional arguments
# @app.get("/get-by-name")
# def get_item(*, name: Optional[str] = None):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#         return {"Data not found"}

# post

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item:Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}

    inventory[item_id] = item
    return inventory[item_id]

# update endpoint
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not exist."}
    
    if item.name != None:
        inventory[item_id].name = item.name 
    if item.price != None:
        inventory[item_id].price = item.price 
    if item.brand != None:
        inventory[item_id].brand = item.brand 
    return inventory[item_id]

#... means required
@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="ID of the item to delete")):
    if item_id not in inventory:
        return {"Error": "ID does not exists."}
    del inventory[item_id]