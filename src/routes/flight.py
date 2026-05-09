from fastapi import APIRouter

from schemas.flight import FlightFiltersDTO, FlightSearchDTO, FlightDataDTO
from schemas.utils.pagination import PaginatedList


router = APIRouter(prefix="/flights", tags=["flight"])

@router.post("/search")
async def get_my_tickets(body: FlightSearchDTO) -> PaginatedList[FlightDataDTO]:
    pass

@router.post("/filter")
async def order_ticket(body: FlightFiltersDTO) -> FlightDataDTO:
    pass

@router.get("/{id}")
async def get_flight_data(
    id: int,
) -> FlightDataDTO:
    pass

@router.get("/{id}/send_mail")
async def send_ticket_on_mail(
    id: int
):
    pass