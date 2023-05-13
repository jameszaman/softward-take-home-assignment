from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, root_validator, validator
from .tenants import TenantSchema

class PropertySchema(BaseModel):
    id: str = Field(..., alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    price: float = Field(...)
    bedrooms: int = Field(...)
    bathrooms: float = Field(...)
    size: float = Field(...)
    location: List[float] = Field(...)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    tenants: List[TenantSchema] = Field(default=[])

    @validator('tenants')
    def check_unique_emails(cls, v):
        email_set = set()
        duplicate_emails = []
        for tenant in v:
            if tenant.email in email_set:
                duplicate_emails.append(tenant.email)
            email_set.add(tenant.email)
        if duplicate_emails:
            raise ValueError(f'Duplicate emails found in tenants: {duplicate_emails}')
        return v
    
    @root_validator(pre=True)
    def map_id_field(cls, values):
        if 'id' not in values and '_id' in values:
            values['id'] = str(values['_id'])
        return values

    class Config:
        schema_extra = {
            "example": {
                "title": "Name Of My House",
                "description": "The most expensive property that money can buy",
                "price": 1000.00,
                "bedrooms": 3,
                "bathrooms": 2.5,
                "size": 420.00,
                "location": [59.9112, 10.7405],
                "tenants": []
            }
        }
