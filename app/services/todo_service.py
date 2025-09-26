from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from app.schemas.todo import Todo, TodoUpdate
from sqlalchemy.orm import Session
from app.models.todo import TodoModel


# todos_db: List[Todo] = []


# Create a new todo
def create_todo_service(db: Session, todo: Todo):
    new_todo = TodoModel(id=todo.id ,task=todo.task, isDone=todo.isDone)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def get_todos(db: Session):
    return db.query(TodoModel).all()


def update_todo_put(db: Session, todo_id: int, todo: Todo):
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    
    if not db_todo:
        return None
    
    db_todo.task = todo.task
    db_todo.isDone = todo.isDone

    db.commit()
    db.refresh(db_todo)

    return db_todo

def update_todo_patch(db: Session, todo_id: int, todo: TodoUpdate):
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()

    if not db_todo:
        return None
    
    if(todo.task != None):
        db_todo.task = todo.task

    if(todo.isDone != None):
        db_todo.isDone = todo.isDone

    db.commit()
    db.refresh(db_todo)

    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()

    if not db_todo:
        return None
    
    db.delete(db_todo)
    db.commit()
    return db_todo

