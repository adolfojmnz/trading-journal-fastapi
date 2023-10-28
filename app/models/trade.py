from sqlalchemy import (
    Column, ForeignKey, Boolean, String, Integer, Float, DateTime
)
from sqlalchemy.orm import relationship

from app.db.session import Base

from app.models.user import User
from app.models.asset import Asset


class Trade(Base):
    __tablename__ = "trade"

    id = Column(Integer, primary_key=True, index=True)
    volume = Column(Float, default=0.01)
    position = Column(String, index=True, nullable=False)
    open_datetime = Column(DateTime, nullable=False)
    close_datetime = Column(DateTime, nullable=False)
    open_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    stop_loss = Column(Float, default=0)
    take_profit = Column(Float, default=0)
    pnl = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id))
    asset_symbol = Column(String, ForeignKey(Asset.symbol))
