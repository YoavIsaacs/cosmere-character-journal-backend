from pydantic import BaseModel

class RelationshipModel(BaseModel):
    characterA: dict # {name: ID}
    characterB: dict # {name: ID}
    relationship_type: str
    description: str
    user_id: str
