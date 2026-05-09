from pydantic import BaseModel

from schemas.seat import SeatDTO


class CreateAirplaneDTO(BaseModel):
    model: str
    capacity: int
    seats: list[SeatDTO] = []

class AirplaneDTO(BaseModel):
    id: int
    model: str
    capacity: int
    # Add other airplane fields as needed
    seats: list[SeatDTO] = []

class EditAirplaneDTO(BaseModel):
    model: str | None = None
    capacity: int | None = None
    seats: list[SeatDTO] = []
    # Add other airplane fields as needed