

class SeatDTO:
    id: int
    airplane_id: int
    user_id: int | None
    row: int
    column: str
    type: str
    occupied: bool = False