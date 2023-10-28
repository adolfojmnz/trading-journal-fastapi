from sqlalchemy import Column, Boolean, String, Integer

from app.db.session import Base


class Asset(Base):
    __tablename__ = "asset"

    symbol = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    pip_on_decimal = Column(Integer, nullable=False)
