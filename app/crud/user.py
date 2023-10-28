from sqlalchemy.orm import Session

from app.models.user import User as UserModel
from app.schemas import user as user_schemas

from app.crud.utils import hash_password


def create_user(db: Session, user: user_schemas.UserCreate):
    user.password = hash_password(user.password)
    db_user = UserModel(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()
