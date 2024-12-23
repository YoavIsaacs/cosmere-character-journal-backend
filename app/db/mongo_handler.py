from typing import List

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

# --------------------------------- CHARACTERS CRUD -------------------------------
async def create_character(character_info: dict) -> dict:
    async with get_db() as db:
        characters = db.characters
        try:
            result = await characters.insert_one(character_info)
            return {"status_code": 201, "message": f"character_id {result.inserted_id} created successfully."}
        except Exception as e:
            return {"status_code": 500, "message": f"internal error creating new character: {e}"}

async def get_character(character_name: str, user_id: ObjectId) -> dict:
    async with get_db() as db:
        characters = db.characters
        try:
            wanted_character = await characters.find_one( {"user_id": user_id, "character_name": character_name})

            if wanted_character is None:
                return {"status_code": 404, "message": "Character not found."}

            return {"status_code": 200, "character_info": wanted_character}
        except Exception as e:
            return {"status_code": 500, "message": f"internal error getting character: {e}"}

async def get_all_characters(user_id: ObjectId) -> dict | List:
    async with get_db() as db:
        characters = db.characters
        try:
            cursor = characters.find({"user_id": user_id})
            character_list = await cursor.to_list(None)
            if not character_list:
                return {"status_code": 404, "message": "User has no characters"}
            return character_list
        except Exception as e:
            return {"status_code": 500, "message": f"internal error getting characters: {e}"}

async def update_character(character_id: ObjectId, new_info: dict) -> dict:
    async with get_db() as db:
        characters = db.characters
        try:
            result = await characters.update_one({"_id": character_id}, {"$set": new_info})

            if result.matched_count == 0:
                return {"status_code": 404, "message": "Character not found."}

            return {"status_code": 200, "message": "Character updated successfully"}

        except Exception as e:
            return {"status_code": 500, "message": f"internal error updating character info: {e}"}

async def delete_character(character_id: ObjectId) -> dict:
    async with get_db() as db:
        characters = db.characters
        try:
            result = await characters.delete_one({"_id": character_id})

            if result.deleted_count == 0:
                return {"status_code": 404, "message": "Character not found."}

            return {"status_code": 200, "message": "Character deleted successfully"}

        except Exception as e:
            return {"status_code": 500, "message": f"internal error deleting character: {e}"}

# --------------------------------- EVENTS CRUD -------------------------------
async def create_event(event_info: dict) -> dict:
    async with get_db() as db:
        events = db.events
        try:
            result = await events.insert_one(event_info)
            return {"status_code": 201, "message": f"event_id {result.inserted_id} created successfully."}
        except Exception as e:
            return {"status_code": 500, "message": f"internal error creating new event: {e}"}

async def get_event(event_name: str, user_id: ObjectId) -> dict:
    async with get_db() as db:
        events = db.events
        try:
            wanted_event = await events.find_one( {"user_id": user_id, "event_name": event_name})

            if wanted_event is None:
                return {"status_code": 404, "message": "Event not found."}

            return {"status_code": 200, "event_info": wanted_event}
        except Exception as e:
            return {"status_code": 500, "message": f"internal error getting event: {e}"}

async def get_all_events(user_id: ObjectId) -> dict | List:
    async with get_db() as db:
        events = db.events
        try:
            cursor = events.find({"user_id": user_id})
            event_list = await cursor.to_list(None)
            if not event_list:
                return {"status_code": 404, "message": "User has no events"}
            return event_list
        except Exception as e:
            return {"status_code": 500, "message": f"internal error getting events: {e}"}

async def update_events(event_id: ObjectId, new_info: dict) -> dict:
    async with get_db() as db:
        events = db.events
        try:
            result = await events.update_one({"_id": event_id}, {"$set": new_info})

            if result.matched_count == 0:
                return {"status_code": 404, "message": "Event not found."}

            return {"status_code": 200, "message": "Event updated successfully"}

        except Exception as e:
            return {"status_code": 500, "message": f"internal error updating event info: {e}"}

async def delete_event(event_id: ObjectId) -> dict:
    async with get_db() as db:
        events = db.evetns
        try:
            result = await events.delete_one({"_id": event_id})

            if result.deleted_count == 0:
                return {"status_code": 404, "message": "Event not found."}

            return {"status_code": 200, "message": "Event deleted successfully"}

        except Exception as e:
            return {"status_code": 500, "message": f"internal error deleting event: {e}"}
