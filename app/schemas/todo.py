# all pydantic modals go here
from pydantic import BaseModel
from typing import Optional


# #step 1 create a pydantic model for todo
class Todo(BaseModel):
    id: int
    task: str
    isDone: bool = False

#pydantic model for todo patch update
class TodoUpdate(BaseModel):
    task: Optional[str] = None
    isDone: Optional[bool] = None


# ---------- Response schemas ----------

class TodoResponse(BaseModel):
    id: int
    task: str
    isDone: bool

    class Config:
        from_attributes = True   # allows returning SQLAlchemy models directly