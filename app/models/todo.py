from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class TodoModel(Base):
    __tablename__ = "todos"

    id =Column(Integer, primary_key = True, index = True)
    task=Column(String, nullable=False)
    isDone=Column(Boolean, default=False)

    