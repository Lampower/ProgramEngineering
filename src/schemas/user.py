from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    email: str
    password: str

class TokenDTO(BaseModel):
    user_id: int
    access_token: str
    refresh_token: str

class UserDTO(BaseModel):
    id: int
    email: str
    # Add other user fields as needed