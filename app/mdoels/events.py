from bson import ObjectId
from pydantic import BaseModel
from typing import List

class EventModel(BaseModel):
    event_name: str
    character_info: List # {name: id} pairs
    event_type: str
    description: str
    world: str
    book: str
    date: int
    user_id: ObjectId
