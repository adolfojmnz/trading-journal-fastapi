from sqlalchemy.orm import Session

from app.schemas import trade as trade_schemas
from app.models.trade import Trade as TradeModel


def create_trade(db: Session, trade: trade_schemas.TradeCreate):
    db_trade = TradeModel(
        id=trade.id,
        volume=trade.volume,
        position=trade.position,
        open_datetime=trade.open_datetime,
        close_datetime=trade.open_datetime,
        open_price=trade.open_price,
        close_price=trade.close_price,
        stop_loss=trade.stop_loss,
        take_profit=trade.take_profit,
        pnl=trade.pnl,
        asset_symbol=trade.asset_symbol,
        user_id=trade.user_id,
    )
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade


def get_trade(db: Session, trade_id: int):
    db_trade = db.query(TradeModel).filter(TradeModel.id == trade_id).first()
    return db_trade


def get_trades(db: Session):
    db_trades = db.query(TradeModel).all()
    return db_trades
