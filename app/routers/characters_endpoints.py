from fastapi import APIRouter, Depends, HTTPException
from app.db import mongo_handler as mg
from app.models

character_endpoints = APIRouter(prefix="characters")


