from fastapi import APIRouter

from schemas.airplane import AirplaneDTO, CreateAirplaneDTO, CreateAirplaneDTO, EditAirplaneDTO
from schemas.user_details import EditUserDetailsDTO, UserDetailsDTO, CreateUserDetailsDTO


# Паспортные данные ес чо
router = APIRouter(prefix="/user_details", tags=["User Details"])

@router.post("")
async def add_user_details(body: CreateUserDetailsDTO) -> UserDetailsDTO:
    pass

@router.get("")
async def get_user_details() -> list[UserDetailsDTO]:
    pass

@router.put("/{id}")
async def edit_user_details(id: int, body: EditUserDetailsDTO) -> UserDetailsDTO:
    pass

@router.delete("/{id}")
async def delete_user_details(id: int) -> None:
    pass
