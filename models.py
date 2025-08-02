# from sqlalchemy import Column, Integer, String, Float
# from db2 import base

# class Item(base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     quantity = Column(Integer, default=0)
#     price = Column(Float, nullable=False)


from sqlalchemy import Column, Integer, String
from db2 import Base

class TodoItem(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, index=True)
