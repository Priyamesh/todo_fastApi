from pydantic import BaseModel
from datetime import datetime


class Todo(BaseModel):
    title: str
    description: str
    completed: bool = False
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))
    # created_at: datetime = datetime.now()
