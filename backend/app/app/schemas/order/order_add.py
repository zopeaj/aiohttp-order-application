from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class Status(str, Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    CANCEL = "CANCEL"

class OrderAdd(BaseModel):
    id: int
    order_id: Optional[int] = None
    date: Optional[datetime] = None
    user: User = None
    product: Product[] = None
    status: Optional[Status] = None


