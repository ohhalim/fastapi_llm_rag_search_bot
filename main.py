from typing import Union 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    pride: float
    is_offer: Union[bool,None] = None

@app.get("/")
def reat_root():
    return {"hello": "world"}

@app.get("/items/{iem_id}")
def read_root(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@ app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
    