from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr
from app.models.order import Order


class UserAdd(BaseModel):
    id: int
    name: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: EmailStr = None
    order: Order[] = None
