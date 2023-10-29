from fastapi import APIRouter
from models.todo import Todo
from schema.schema import list_sirial
from config.database import collection_name
from bson import ObjectId
# from schema.schema import


router =APIRouter()

@router.get("/")
async def get_todo():
    todos =list_sirial(collection_name.find())
    return todos

@router.post("/")
async def insert_todo(todo:Todo):
    collection_name.insert_one(dict(todo))