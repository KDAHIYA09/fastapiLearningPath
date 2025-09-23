from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#todo try dummy

#step 1 create a pydantic model for todo
class Todo(BaseModel):
    id: int
    task: str
    isDone: bool = False

class TodoUpdate(BaseModel):
    task: Optional[str] = None
    isDone: Optional[bool] = None


# for basic we will use in app memory
todos = []

#1st crud - c for create 
@app.post("/todos/")
def create_todo(todo: Todo):
    #first check if todo already exists
    # for loop syntax in python for iterating
    for existing in todos:
        if existing.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo with same id already exists!!")
        
    
    todos.append(todo)
    return{"message": "Todo created successfully", "todo": todo}


#2nd crud - r for read 
@app.get("/todos/")
def get_todos():
    return {"todos": todos}

#2nd part b crud - r for read by id
@app.get("/todos/{todo_id}/")
def get_todo_by_id(todo_id: int):
    for existing in todos:
        if existing.id == todo_id:
            return {"message": "Todo with specified id found successfully", "todo": existing}
            
    raise HTTPException(status_code=400, detail="No such item exists")


#3rd crud - u for update 
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for existing in todos:
        if existing.id == todo_id:
            existing.task = todo.task
            existing.isDone = todo.isDone
            return {"message": "Todo updated successfully", "todo": existing}
    
    raise HTTPException(status_code=400, detail="No such item exists")


#3rd part b - crud u for update part b update partially patch example
@app.patch("/todos/{todo_id}")
def update_todo_partially(todo_id: int, todo_update: TodoUpdate):
    for existing in todos:
        if existing.id == todo_id:
            if todo_update.task is not None:
                existing.task = todo_update.task
            
            if todo_update.isDone is not None:
                existing.isDone = todo_update.isDone
            return {"message": "Todo updated successfully", "todo": existing}
    
    raise HTTPException(status_code=400, detail="No todo with specified id exists")



#4 crud d for delete
@app.delete("/todos/{todo_id}/")
def delete_todo(todo_id: int):
    for existing in todos:
        if existing.id == todo_id:
            todos.remove(existing)
            return {"message": "Todo deleted successfully", "todo": existing}
    
    raise HTTPException(status_code=404, detail="No such todo exists")







        











# @app.get("/greet")
# def get_name(name : str):
#     return {"message": f"hello, {name}"}

# class User(BaseModel):
#     name: str
#     age: int
#     email: str

# @app.post("/users/")
# def create_user(user: User):
#     return {"message": "User created successfully", "user": user}

# @app.get("/")
# def read_root():
#     return {"message": "Hello, world!!"}

# @app.get("/hello/{name}")
# def greeting(name: str):
#     return {"message": f"Hello, {name}!! Have a nice day!"}

# @app.get("/bye-bye/{name}")
# def goodbye(name: str):
#     return {"message": f"Goodbye, {name}! See you soon! Have a nice day ^_^"}

# @app.get("/subjects")
# def subjectsList():
#     return {"subjects": ["Math", "Physics", "Chemistry", "Biology", "English"]}

# @app.get("/items/")
# def getItems(itemId: int, itemValue: str | None = None):
#     return {"itemId" : itemId, "itemValue" : itemValue}


# #pydantic model

# class Item(BaseModel):
#     name: str
#     price: float
#     inStock: bool = True
#     color: str

# @app.post("/items/")
# def createItem(item: Item):
#     return {"message": "item received", "item": item}