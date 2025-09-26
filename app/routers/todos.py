from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.todo import TodoModel
from app.schemas.todo import Todo, TodoResponse, TodoUpdate
from app.services import todo_service
from typing import List

router = APIRouter()

@router.post("/", response_model=TodoResponse)
def create_todo(todo: Todo, db: Session = Depends(get_db)):
    return todo_service.create_todo_service(db, todo)


@router.get("/", response_model=List[TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return todo_service.get_todos(db)


@router.put("/{todo_id}", response_model=TodoResponse)
def update_put_todo(todo_id: int, todo: Todo, db: Session = Depends(get_db)):
    updated = todo_service.update_todo_put(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@router.patch("/{todo_id}", response_model=TodoResponse)
def update_patch_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated = todo_service.update_todo_patch(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@router.delete("/{todo_id}", response_model=TodoResponse)
def delete_todo_endpoint(todo_id: int, db: Session = Depends(get_db)):
    deleted = todo_service.delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return deleted
    
    
