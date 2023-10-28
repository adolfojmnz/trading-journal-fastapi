from pydantic import BaseModel


class AssetBase(BaseModel):
    symbol: str
    name: str
    pip_on_decimal: int


class Asset(AssetBase):
    """ Properties to return via API on GET requests. """

    class Config:
        from_attributes = True


class AssetCreate(AssetBase):
    """ Properties to receive via API on POST requests. """
    pass
