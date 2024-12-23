from motor import motor_asyncio
from contextlib import contextmanager


@contextmanager
def get_db() -> motor_asyncio.AsyncIOMotorClient:
    client = motor_asyncio.AsyncIOMotorClient("localhost", 27017)
    db = client.cosemere_backend
    try:
        print("yielding db...")
        yield db
    finally:
        print("closing db...")
        client.close()
