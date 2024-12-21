from pydantic import BaseModel
from typing import List

class CharacterModel(BaseModel):
    full_name: str
    homeWorld: str
    abilities: str
    notableItems: List
    age: int
    