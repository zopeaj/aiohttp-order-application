from pydantic import BaseModel, EmailStr
from typing import Any, List, Optional

class UserAdd(BaseModel):
    id: int
    name: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: EmailStr = None
    order: Order[] = None


class UserUpdate(BaseModel):
    pass

