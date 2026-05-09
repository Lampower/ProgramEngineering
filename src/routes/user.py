from fastapi import APIRouter

from schemas.user import EditUserDTO, TokenDTO, UserCreateDTO, UserDTO


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
async def register_user(body: UserCreateDTO) -> TokenDTO:
    pass

@router.post("/login")
async def login_user(body: UserCreateDTO) -> TokenDTO:
    pass

@router.get("/me")
async def get_me() -> UserDTO:
    pass

@router.put("/edit")
async def edit(bodt: EditUserDTO) -> UserDTO:
    pass

# если все равно можно без рефреша сделать, по факту просто безопасность теряем
@router.get("/refresh")
async def refresh_token() -> TokenDTO:
    pass