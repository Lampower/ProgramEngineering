from fastapi import APIRouter

from schemas.ticket import TicketDTO
from schemas.user import TokenDTO, UserCreateDTO, UserDTO


router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.get("/get_my_tickets")
async def get_my_tickets() -> list[TicketDTO]:
    pass

@router.post("/order")
async def order_ticket() -> TicketDTO:
    pass

@router.get("/{id}")
async def get_ticket(
    id: int
) -> TicketDTO:
    pass

@router.delete("/{id}/cancel")
async def cancel_ticket(
    id: int,
) -> None:
    pass

@router.get("/{id}/send_mail")
async def send_ticket_on_mail(
    id: int
) -> None:
    pass