from bson import ObjectId
from fastapi import HTTPException

from app.db import get_db

# --------------------------------- USERS CRUD -------------------------------
async def create_user(username: str, email: str, hashed_password: str) -> dict:
    async with get_db() as db:
        users = db.users_info
        user_info = {
            "username": username,
            "email": email,
            "hashed_password": hashed_password
        }
        try:
            result = await users.insert_one(user_info)
            return {"status_code": 201, "message": f"user_id {result.inserted_id} created successfully."}
        except Exception as e:
            return {"status_code": 500, "message": f"internal error creating new user: {e}"}



async def get_user(username: str, hashed_password: str) -> dict:
    async with get_db() as db:
        users = db.users_info
        try:
            wanted_user = await users.find_one( {"username": username, "hashed_password": hashed_password})

            if wanted_user is None:
                return {"status_code": 404, "message": "User not found."}

            return {"status_code": 200, "user_info": wanted_user}
        except Exception as e:
            return {"status_code": 500, "message": f"internal error getting user: {e}"}


async def update_user(user_id: ObjectId, new_info: dict) -> dict:
    async with get_db() as db:
        users = db.users_info
        try:
            result = await users.update_one({"_id": user_id}, {"$set": new_info})

            if result.matched_count == 0:
                return {"status_code": 404, "message": "User not found."}

            return {"status_code": 200, "message": "User updated successfully"}

        except Exception as e:
            return {"status_code": 500, "message": f"internal error updating user info: {e}"}


async def delete_user(user_id: ObjectId) -> dict:
    async with get_db() as db:
        users = db.users_info
        try:
            result = await users.delete_one({"_id": user_id})

            if result.deleted_count == 0:
                return {"status_code": 404, "message": "User not found."}

            return {"status_code": 200, "message": "User deleted successfully"}

        except Exception as e:
            return {"status_code": 500, "message": f"internal error deleting user info: {e}"}
