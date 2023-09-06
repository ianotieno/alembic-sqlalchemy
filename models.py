from sqlalchemy import Column
from sqlalchemy.orm import declarative_base
Base =declarative_base()

class UserModel(Base):
    id=Column(Integer,primary_key=True)