from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/greet")
def get_name(name : str):
    return {"message": f"hello, {name}"}


class User(BaseModel):
    name: str
    age: int
    email: str


@app.post("/users/")
def create_user(user: User):
    return {"message": "User created successfully", "user": user}









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