from enum import Enum
from typing import List

from pydantic import BaseModel

class PetstoreRequestModelPet(BaseModel):
    id: int = None
    category: 'PetstoreRequestModelCategory' = None
    name: str = None
    photoUrls: List[str] = None
    tags: List[str] = None
    status: 'PetstoreRequestEnumStatus' = None

class PetstoreRequestModelCategory(BaseModel):
    id: int
    name: str

class PetstoreRequestEnumStatus(Enum):
    AVAILABLE = 'available'
    PENDING = 'pending'
    SOLD = 'sold'
    STRING = 'string'

class PetstoreResponseErrorModel(BaseModel):
    code: int
    type: str
    message: str