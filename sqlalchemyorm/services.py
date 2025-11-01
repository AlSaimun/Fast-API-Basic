from models import User
from db import SessionLocal
from sqlalchemy import select

# insert data
def create_user(name: str, email: str):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        # session.refresh(user)
        # return user


# get single user
def get_user(user_id: int):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        return user

# get all user
def get_all_user():
    with SessionLocal() as session:
        stmt = select(User)
        users = session.scalars(stmt).all()
        return users
    
# update user
def update_user(user_id: int, new_email: str):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            user.email = new_email
            session.commit()

            return user
        
        return None
    
# delete user
def delete_user(user_id: int):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False