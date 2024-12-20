from pydantic import BaseModel, EmailStr

class Users(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
