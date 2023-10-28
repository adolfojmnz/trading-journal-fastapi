from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """ Common properties. """
    username: str
    first_name: str
    last_name: str
    email: EmailStr


class User(UserBase):
    """ Properties to return via API on GET requests. """
    id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    """ Properties to receive via API on POST requests. """
    password: str
