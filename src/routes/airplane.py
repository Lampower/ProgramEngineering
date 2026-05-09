from fastapi import APIRouter

from schemas.airplane import AirplaneDTO, CreateAirplaneDTO, CreateAirplaneDTO, EditAirplaneDTO
from schemas.user import TokenDTO, UserCreateDTO, UserDTO


router = APIRouter(prefix="/airplanes", tags=["airplanes"])

@router.post("/create")
async def create_airplane(body: CreateAirplaneDTO) -> AirplaneDTO:
    pass

@router.post("/edit")
async def edit_airplane(body: EditAirplaneDTO) -> AirplaneDTO:
    pass

@router.get("")
async def get_airplane() -> AirplaneDTO:
    pass
