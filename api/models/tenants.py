from pydantic import BaseModel, Field, validator

class TenantSchema(BaseModel):
    name: str = Field(..., example="John Smith")
    email: str = Field(..., example="john.smith@example.com")
    phone: str = Field(..., example="123-456-7890")
    lease_start: str = Field(..., example="2024-01-01")
    lease_end: str = Field(..., example="2025-01-01")

    class Config:
        arbitrary_types_allowed = True


