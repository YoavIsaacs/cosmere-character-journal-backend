from bson import ObjectId
from pydantic import BaseModel
from typing import List

class CharacterModel(BaseModel):
    full_name: str
    home_world: str
    abilities: List
    notable_items: List
    age: int
    user_id: ObjectId