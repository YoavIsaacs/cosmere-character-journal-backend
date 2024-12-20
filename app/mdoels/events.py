from pydantic import BaseModel

class EventModel(BaseModel):
    character_name: str
    event_type: str
    description: str
    world: str
    book: str
    date: int
