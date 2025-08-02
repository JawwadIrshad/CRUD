
# from fastapi import FastAPI
# from db2 import base, engine
# from items import Item

# base.metadata.create_all(bind=engine)

# app = FastAPI()
# app.include_router(Item.routes, prefix="/Item", tags=["Item"])

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Enhanced FastAPI Todo App!"}



from fastapi import FastAPI
from db2 import Base, engine
from routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(items.router, prefix="/todos", tags=["Todos"])
@app.get("/")
def read_root():
    return {"message": "Welcome to the Enhanced FastAPI Todo App!"}
