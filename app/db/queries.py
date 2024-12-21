from app.db import get_db
from psycopg2.extensions import cursor

def add_character_to_db(user_id: str, full_name: str = "", home_world: str = "", abilities: str = "",
                        age: int = 0, notable_items: dict = None, cur: cursor = None):
    if notable_items is None:
        notable_items = {}

    if cur is None:
        print("Error, no cursor given.")
        return

    query_str = f"""INSERT INTO characters (full_name, homeworld, abilities, age, notableItems, user_id)
                    VALUES ({full_name}, {home_world}, {abilities}, {age}, {notable_items}, {user_id})
"""

    cur.execute(query=query_str)

def add_event_to_db(user_id: str, character: str = "", event_type: str = "", description: str = "", world: str = "",
                    date: int = 0, book: str = "", cur: cursor = None) -> None:
    if cur is None:
        print("Error, no cursor given.")
        return

    query_str = f"""INSERT INTO events (character, eventType, description, world, date, book, user_id)
                    VALUES ({character}, {event_type}, {description}, {world}, {date}, {book}, {user_id})
"""

    cur.execute(query=query_str)

def add_relationship_to_db(user_id: str, character_a: str = "", character_b: str = "", relationship_type: str = "",
                           description: str = "", cur: cursor = None) -> None:
    if cur is None:
        print("Error, no cursor given.")
        return

    query_str = f""" INSERT INTO relationships (characterA, characterB, relationshipType, description, user_id)
                     VALUES ({character_a}, {character_b}, {relationship_type}, {description}, {user_id})
    """

    cur.execute(query=query_str)

def insert_user_to_db(username: str = "", email: str = "", hashed_password: str = "", cur: cursor = None) -> None:
    if cur is None:
        print("Error, no cursor given.")
        return

    query_str = f"""INSERT INTO users (username, email, hashedPassword)
                    VALUES ({username}, {email}, {hashed_password})
       """

    cur.execute(query=query_str)

    
