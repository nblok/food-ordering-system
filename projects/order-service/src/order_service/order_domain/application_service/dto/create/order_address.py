from pydantic import BaseModel, ConfigDict, Field


class OrderAddress(BaseModel):
    model_config = ConfigDict(frozen=True)
    street: str = Field(max_length=50)
    postal_code: str = Field(max_length=10)
    city: str = Field(max_length=50)
