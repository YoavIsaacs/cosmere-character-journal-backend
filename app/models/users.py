from pydantic import BaseModel, EmailStr

class UsersModel(BaseModel):
    username: str
    email: EmailStr
    password: str
