from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


todos: list[Todo] = [
    Todo(id=1, title="Learn Python", completed=False),
    Todo(id=2, title="Learn FastAPI", completed=True),
    Todo(id=3, title="Learn Vue", completed=False),
    Todo(id=4, title="Learn Docker", completed=False),
    Todo(id=5, title="Learn Kubernetes", completed=False),
    Todo(id=6, title="Learn Git", completed=False),
    Todo(id=7, title="Learn SQL", completed=False),
    Todo(id=8, title="Learn NoSQL", completed=False),
    Todo(id=9, title="Learn MongoDB", completed=False),
    Todo(id=10, title="Learn Redis", completed=False),
]


@app.get("/", response_model=list[Todo])
def getAlltodos():
    return todos


@app.get("/{item_id}", response_model=Todo)
def getTodo(item_id: int):
    todo = None
    for Todo in todos:
        if Todo.id == item_id:
            todo = Todo
            break
    return todo


@app.post("/", response_model=Todo)
def createTodo(todo: Todo):
    todos.append(todo)
    return todo


@app.put("/{todo_id}", response_model=Todo)
def updateTodo(todo_id: int, updatedTodo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updatedTodo
            break

    return updatedTodo


@app.delete("/{todo_id}", response_model=dict)
def deleteTodo(todo_id: int):
    delTodo = None
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            delTodo = todos[index]
            del todos[index]
            break

    return {"message": "Todo deleted successfully", "todo": delTodo}
