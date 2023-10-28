from sqlalchemy import Column, Boolean, String, Integer

from app.db.session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
