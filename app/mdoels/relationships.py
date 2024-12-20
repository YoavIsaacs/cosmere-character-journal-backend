from pydantic import BaseModel

class RelationshipModel(BaseModel):
    characterA: str
    characterB: str
    relationship_type: str
    description: str
