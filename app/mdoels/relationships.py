from bson import ObjectId
from pydantic import BaseModel

class RelationshipModel(BaseModel):
    characterA: str
    characterB: str
    relationship_type: str
    description: str
    user_id: ObjectId
