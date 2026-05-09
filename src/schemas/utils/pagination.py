from typing import TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class PaginatedList[T](BaseModel):
    data: list[T]
    total: int = 0
    elements_on_page: int = 0
    page_size: int = 0     

class RangeRequestDTO(BaseModel):
    page: int
    amount: int
