from fastapi import APIRouter

from schemas.airplane import AirplaneDTO, CreateAirplaneDTO, CreateAirplaneDTO, EditAirplaneDTO
from schemas.user import TokenDTO, UserCreateDTO, UserDTO


router = APIRouter(prefix="/airplanes", tags=["airplanes"])

@router.get("/{id}")
async def get_airplane(id: int) -> AirplaneDTO:
    pass
