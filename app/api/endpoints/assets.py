from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from app.crud import asset as asset_crud
from app.schemas import asset as asset_schemas

from app.api.deps import get_db
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("", status_code=201, response_model=asset_schemas.Asset)
def create_asset(asset: asset_schemas.AssetCreate,
                 db: Session = Depends(get_db)):
    if asset_crud.get_asset(db, asset_symbol=asset.symbol):
        raise HTTPException(status_code=400,
                            detail="Asset's symbol already registered")
    return asset_crud.create_asset(db, asset)


@router.get("/{asset_symbol}", response_model=asset_schemas.Asset)
def get_asset(asset_symbol: str, db: Session = Depends(get_db)):
    db_asset = asset_crud.get_asset(db, asset_symbol)
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset


@router.get("", response_model=list[asset_schemas.Asset])
def get_assets(db: Session = Depends(get_db)):
    db_assets = asset_crud.get_assets(db)
    return db_assets
