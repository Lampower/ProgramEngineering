
from pydantic import BaseModel


class TicketDTO(BaseModel):
    id: int
    title: str
    description: str
    status: str
    