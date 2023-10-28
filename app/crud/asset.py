from sqlalchemy.orm import Session

from app.schemas import asset as asset_schemas
from app.models.asset import Asset as AssetModel


def create_asset(db: Session, asset: asset_schemas.AssetCreate):
    db_asset = AssetModel(
        symbol=asset.symbol,
        name=asset.name,
        pip_on_decimal=asset.pip_on_decimal,
    )
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset


def get_asset(db: Session, asset_symbol: str):
    db_asset = db.query(AssetModel).filter(AssetModel.symbol == asset_symbol).first()
    return db_asset


def get_assets(db: Session):
    db_assets = db.query(AssetModel).all()
    return db_assets
