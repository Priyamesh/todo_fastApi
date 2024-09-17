from fastapi import FastAPI, APIRouter, HTTPException
from bson.objectid import ObjectId

# from datetime import datetime

from configurations import collections
from database.schemas import individual_data, all_data
from database.models import Todo

app = FastAPI()
router = APIRouter()


@router.get("/")
async def getAllTodos():
    data = collections.find()
    return all_data(data)


@router.post("/")
async def createTodo(newtask: Todo):
    try:
        res = collections.insert_one(dict(newtask))
        return {
            "status_code": 200,
            "data": individual_data(collections.find_one({"_id": res.inserted_id})),
        }
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")


@router.put("/{todo_id}")
async def updateTodo(todo_id: str, updatedTask: Todo):
    try:
        id = ObjectId(todo_id)
        exe_todo = collections.find_one({"_id": id})

        if exe_todo is None:
            return HTTPException(status_code=404, detail="Task does not exist")

        # TODO add updated_at field
        # updatedTask.updated_at = datetime.timestamp(datetime.now())
        res = collections.update_one({"_id": id}, {"$set": dict(updatedTask)})

        # TODO add updated task in return body
        return {
            "status_code": 200,
            "data": "updated data",
        }
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")


@router.delete("/{todo_id}")
async def deleteTodo(todo_id: str, updatedTask: Todo):
    try:
        id = ObjectId(todo_id)
        exe_todo = collections.find_one({"_id": id})

        if exe_todo is None:
            return HTTPException(status_code=404, detail="Task does not exist")

        res = collections.delete_one({"_id": id})
        return {
            "status_code": 200,
            "data": "Deleted Todo",
        }
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")


app.include_router(router)
