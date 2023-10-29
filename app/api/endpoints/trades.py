from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from app.crud import trade as trade_crud
from app.schemas import trade as trade_schemas

from app.api.deps import get_db
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("", response_model=trade_schemas.Trade)
def create_trade(trade: trade_schemas.TradeCreate,
                 db: Session = Depends(get_db)):
    if trade_crud.get_trade(db, trade.id) is not None:
        raise HTTPException(
            status_code=400, detail="Trade's id already registered"
        )
    return trade_crud.create_trade(db, trade)


@router.get("", response_model=list[trade_schemas.Trade])
def get_trades(db: Session = Depends(get_db)):
    db_trades = trade_crud.get_trades(db)
    return db_trades


@router.get("/{tarde_id}", response_model=trade_schemas.Trade)
def get_trade(trade_id: int, db: Session = Depends(get_db)):
    db_trade = trade_crud.get_trade(db, trade_id)
    if not db_trade:
        raise HTTPException(status_code=404, detail="Trade not found")
    return db_trade
