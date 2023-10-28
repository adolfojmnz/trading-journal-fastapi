from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from app.crud import user as user_crud
from app.schemas import user as user_schemas
from app.models.user import User as UserModel

from app.api.deps import get_db
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    if user_crud.get_user_by_email(db, email=user.email) is not None:
        raise HTTPException(status_code=400, detail="Email already registered")
    if user_crud.get_user_by_username(db, username=user.username) is not None:
        raise HTTPException(status_code=400, detail="Username already registered")
    return user_crud.create_user(db, user)


@router.get("/{user_id}", response_model=user_schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("", response_model=list[user_schemas.User])
def get_users(db: Session = Depends(get_db)):
    db_users = user_crud.get_users(db)
    return db_users
