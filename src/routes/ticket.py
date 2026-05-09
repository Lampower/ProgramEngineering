from fastapi import APIRouter

from schemas.user import TokenDTO, UserCreateDTO, UserDTO


router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.get("/get_my_tickets")
async def get_my_tickets() -> TokenDTO:
    pass

@router.post("/order")
async def order_ticket() -> TokenDTO:
    pass

@router.delete("/{ticket_id}/cancel")
async def cancel_ticket(
    ticket_id: int,
    body: UserCreateDTO
) -> TokenDTO:
    pass
