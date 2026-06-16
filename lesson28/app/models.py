from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Option[int] = None
    name: str
    description: Optional[str] = None