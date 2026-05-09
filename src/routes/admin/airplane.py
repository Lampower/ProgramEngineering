from fastapi import APIRouter

from schemas.airplane import AirplaneDTO, CreateAirplaneDTO, EditAirplaneDTO
from schemas.utils.pagination import PaginatedList

router = APIRouter(prefix="/airplanes", tags=["Admin Airplanes"])

@router.get("")
async def get_airplanes(page: int, amount: int) -> PaginatedList[AirplaneDTO]:
    pass

@router.post("/create")
async def create_airplane(body: CreateAirplaneDTO) -> AirplaneDTO:
    pass

@router.post("/edit")
async def edit_airplane(body: EditAirplaneDTO) -> AirplaneDTO:
    pass


@router.delete("/{id}")
async def delete_airplane(id: int):
    pass
