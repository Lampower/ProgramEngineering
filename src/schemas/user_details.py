from pydantic import BaseModel

class UserDetailsDTO(BaseModel):
    id: int
    type: str
    serial: int

class CreateUserDetailsDTO(BaseModel):
    type: str
    serial: int

class EditUserDetailsDTO(BaseModel):
    type: str
    serial: int