from pydantic import BaseModel, Field


class OrderAddress(BaseModel, frozen=True):
    street: str = Field(max_length=50)
    postel_code: str = Field(max_length=10)
    city: str = Field(max_length=50)