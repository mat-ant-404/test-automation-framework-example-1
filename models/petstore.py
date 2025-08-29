from enum import Enum
from typing import List, Union

from pydantic import BaseModel

class PetstoreRequestModelPet(BaseModel):
    id: Union[str, int, None] = None
    category: Union['PetstoreRequestModelCategory', None, str, int] = None
    name: Union[str, int, None] = None
    photoUrls: Union[List[str], None] = None
    tags: Union[List['PetstoreRequestModelTag'], None, str] = None
    status: Union[str, int, None] = None

class PetstoreRequestModelCategory(BaseModel):
    id: Union[str, int, None] = None
    name: Union[str, int, None] = None

class PetstoreRequestModelTag(BaseModel):
    id: Union[str, int, None] = None
    name: Union[str, int, None] = None

class PetstoreRequestEnumStatus(Enum):
    AVAILABLE = 'available'
    PENDING = 'pending'
    SOLD = 'sold'
    UNKNOWN_STRING = 'unknown_string'

class PetstoreResponseErrorModel(BaseModel):
    code: int
    type: str
    message: str