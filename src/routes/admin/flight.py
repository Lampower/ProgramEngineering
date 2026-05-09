from fastapi import APIRouter

from schemas.flight import CreateFlightDataDTO, EditFlightDataDTO, FlightDataDTO

router = APIRouter(prefix="/flights", tags=["Admin Flights"])

@router.post("/create")
async def create(body: CreateFlightDataDTO) -> FlightDataDTO:
    pass

@router.post("/edit")
async def edit(body: EditFlightDataDTO) -> FlightDataDTO:
    pass


@router.delete("/{id}")
async def delete(id: int):
    pass