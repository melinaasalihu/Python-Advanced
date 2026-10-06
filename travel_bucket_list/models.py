from pydantic import BaseModel, Field
from typing import Optional


# =========================
# CREATE
# =========================

class DestinationCreate(BaseModel):

    country: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)

    budget: float = 0

    priority: str = "Medium"

    status: str = "Wishlist"

    travel_date: str = ""

    notes: str = ""


# =========================
# UPDATE
# =========================

class DestinationUpdate(BaseModel):

    country: Optional[str] = None
    city: Optional[str] = None

    budget: Optional[float] = None

    priority: Optional[str] = None

    status: Optional[str] = None

    travel_date: Optional[str] = None

    notes: Optional[str] = None


# =========================
# RESPONSE
# =========================

class DestinationResponse(BaseModel):

    id: int

    country: str
    city: str

    budget: float

    priority: str
    status: str

    travel_date: str
    notes: str

    capital: str
    region: str
    currency: str
    flag: str
