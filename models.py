from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker 
Base =declarative_base()

class UserModel(Base):
    __tablename__="user"

    id=Column(Integer,primary_key=True)
    first_name=Column(String,nullable=False)
    last_name=Column(String,nullable=False)
    birth= Column(DateTime)
    created =Column(DateTime,default=datetime.utcnow)
users=[
    UserModel(first_name='ian', last_name='otieno',birth=datetime(2003,7,8)),
    UserModel(first_name='hellen', last_name='wamaitha',birth=datetime(2004,7,6)),

]
session_maker= sessionmaker(bind=create_engine('sqlite:///models.db'))

def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
            session.commit()

create_users()            