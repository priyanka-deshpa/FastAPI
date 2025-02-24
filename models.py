from pydantic import BaseModel, Field
from typing import Optional

class Vendor(BaseModel):
    id: int
    name: str = Field(..., example="ABC Suppliers")
    contact: str = Field(..., example="contact@abc.com")
    address: str = Field(..., example="123 Market Street, NY")
    rating: Optional[float] = Field(None, ge=1, le=5, example=4.5)

class VendorUpdate(BaseModel):
    name: Optional[str]
    contact: Optional[str]
    address: Optional[str]
    rating: Optional[float]
