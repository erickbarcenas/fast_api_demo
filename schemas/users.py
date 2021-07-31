from typing import List
from pydantic import BaseModel, EmailStr


class UserDto(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_active: bool
    photo: List[str]
