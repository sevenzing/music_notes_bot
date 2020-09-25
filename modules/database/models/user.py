from typing import Union
from sqlalchemy import Column, Integer, String
from modules.database import db_handler, Base
from sqlalchemy.exc import IntegrityError


class User(Base):
    __tablename__ = 'users'
    
    _id = Column(Integer, primary_key=True)
    username = Column(String(40))
    string = Column(String(400))

    def update(self, **kwargs):
        return update_user(chat_id=_id, **kwargs)

    def __repr__(self):
       return f"User(_id={self._id}, username={self.username}, string={self.string})"

@db_handler()
def create_if_not_exists(session, chat_id, **kwargs):
    try:
        user = User(_id=chat_id, **kwargs)
        session.add(user)
        session.commit()
    except IntegrityError:
        # user already exists
        pass
    finally:
        user = get_user(session, chat_id=chat_id)
    return user

@db_handler(commit=True)
def update_user(session, chat_id, **kwargs):
    user = get_user(session, chat_id=chat_id)
    for arg in kwargs:
        user[arg] = kwargs[arg]
    
def get_user(session, chat_id):
    return session.query(User).filter_by(_id=chat_id).first()

