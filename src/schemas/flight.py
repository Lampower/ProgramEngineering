from datetime import datetime
from pydantic import BaseModel

from schemas.utils.pagination import RangeRequestDTO

class FlightFiltersDTO(RangeRequestDTO):
    to_id: int | None = None
    time_from: datetime | None = None
    time_to: datetime | None = None

class FlightSearchDTO(RangeRequestDTO):
    flight_code: str
    page: int
    amount: int

class FlightDataDTO(BaseModel):
    id: int
    code: str
    airplane_id: int

class CreateFlightDataDTO(BaseModel):
    airplane_id: int
    code: str
    to_id: int
    flight_time: datetime

class EditFlightDataDTO(BaseModel):
    airplane_id: int
    code: str
    to_id: int
    flight_time: datetime