from fastapi import APIRouter, HTTPException, Depends
from app.models.users import UsersModel
from app.utils.auth import hash_password, create_access_token

auth_router = APIRouter()

@auth_router.post("/register")
async def register_user(user: UsersModel) -> dict:
    # TODO: add the new user to the database

    hashed_password = hash_password(user.password)


    return {
        "message": "User registered successfully"
    }

@auth_router.post("/login")
async def login_user(username: str, password: str) -> dict:
    # TODO: VERIFY USERNAME AND PASSWORD FORM THE DATABASE

    token = create_access_token(data={"sub": username})
    return {
        "access_token": token,
        "token_type": "bearer"
    }


