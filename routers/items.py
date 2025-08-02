
# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.orm import Session
# from typing import List
# from models import Item
# from schema import Create,update,out
# from db2 import get_db

# router = APIRouter()

# @router.post("/", response_model=out)
# def create(items: Create, db: Session = Depends(get_db)):
#     db_todo = Item(**items.dict())
#     db.add(db_todo)
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo

# @router.get("/", response_model=List[out])
# def read(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return db.query(Item).offset(skip).limit(limit).all()

# @router.get("/{todo_id}", response_model=out)
# def read(todo_id: int, db: Session = Depends(get_db)):
#     items = db.query(Item).filter(Item.id == todo_id).first()
#     if not items:
#         raise HTTPException(status_code=404, detail="items not found")
#     return items

# @router.put("/{todo_id}", response_model=out)
# def update(todo_id: int, items: update, db: Session = Depends(get_db)):
#     db_todo = db.query(Item).filter(Item.id == todo_id).first()
#     if not db_todo:
#         raise HTTPException(status_code=404, detail="items not found")
#     for key, value in items.dict(exclude_unset=True).items():
#         setattr(db_todo, key, value)
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo

# @router.delete("/{todo_id}", response_model=dict)
# def delete(todo_id: int, db: Session = Depends(get_db)):
#     db_todo = db.query(Item).filter(Item.id == todo_id).first()
#     if not db_todo:
#         raise HTTPException(status_code=404, detail="items not found")
#     db.delete(db_todo)
#     db.commit()
#     return {"detail": "items deleted"}



from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from models import TodoItem
from schema import TodoCreate, TodoUpdate, TodoOut
from db2 import get_db

router = APIRouter()

@router.post("/", response_model=TodoOut)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = TodoItem(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/", response_model=List[TodoOut])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(TodoItem).offset(skip).limit(limit).all()

@router.get("/{todo_id}", response_model=TodoOut)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.delete("/{todo_id}", response_model=dict)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"detail": "Todo deleted"}
