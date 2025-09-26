from app.db.database import Base, engine
from app.models.todo import TodoModel

Base.metadata.create_all(bind=engine)

print("database tablel clreated successfully")