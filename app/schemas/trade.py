from typing import Optional

from datetime import datetime

from pydantic import BaseModel


class TradeBase(BaseModel):
    """ Common properties. """
    id: int
    volume: float
    position: str
    open_datetime: datetime
    close_datetime: datetime
    open_price: float
    close_price: float
    stop_loss: Optional[float] = 0
    take_profit: Optional[float] = 0
    pnl: float
    asset_symbol: str
    user_id: int


class Trade(TradeBase):
    """ Properties to return via API on GET requests. """

    class Config:
        from_attributes = True


class TradeCreate(TradeBase):
    """ Properties to receive via API on POST requests. """
    pass
