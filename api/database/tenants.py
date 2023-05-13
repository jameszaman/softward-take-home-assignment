from typing import Optional
from bson import ObjectId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from api.database.properties import PropertyDB
from config import MONGO_URI, MONGO_DB_NAME

from ..models.tenants import TenantSchema
from ..models.properties import PropertySchema


class TenantDB:
    client = None
    db = None

    @classmethod
    def initialize(cls):
        cls.client = AsyncIOMotorClient(str(MONGO_URI))
        cls.db = cls.client[MONGO_DB_NAME]

    @classmethod
    async def add_tenant_to_property(cls, id: str, tenant: TenantSchema):
        property = None
        try:
            property = await cls.db.properties.find_one({"_id": ObjectId(id)})
            if not property:
                raise HTTPException(404, "Property not found")
        except:
            raise HTTPException(400, "Please give proper ObjectId")
        
        property["tenants"].append(tenant)
        property_dict = PropertySchema(**property).dict()
        result = await cls.db.properties.replace_one(
            {"_id": ObjectId(id)}, property_dict
        )
        
        if result.modified_count == 0:
            raise HTTPException(304, "Tenant not modified")
        return property_dict

    @classmethod
    async def delete_tenant_from_property(cls, property_id: str, tenant_email: str):
        property = None
        try:
            property = await cls.db.properties.find_one({"_id": ObjectId(property_id)})
            if not property:
                raise HTTPException(404, "Property not found")
        except:
            raise HTTPException(400, "Please give proper ObjectId")
        
        tenants = property.get("tenants", [])
        
        for i, tenant in enumerate(tenants):
            if str(tenant.get("email")) == tenant_email:
                del tenants[i]
                property["tenants"] = tenants
                property_dict = PropertySchema(**property).dict()
                result = await cls.db.properties.replace_one(
                    {"_id": ObjectId(property_id)}, property_dict
                )
                if result.modified_count == 0:
                    raise HTTPException(304, "Tenant not modified")
                return property_dict
        raise HTTPException(404, "Tenant not found")


    @classmethod
    async def get_tenant_from_property(cls, property_id: str, tenant_email: str) -> TenantSchema:
        property = None
        try:
            property = await cls.db.properties.find_one({"_id": ObjectId(property_id)})
        except:
            raise HTTPException(400, "Please give proper ObjectId")
        
        if not property:
            raise HTTPException(404, "Property not found")

        for tenant in property.get("tenants", []):
            if tenant.get("email") == tenant_email:
                return TenantSchema(**tenant)
        
        raise HTTPException(404, "Tenant not found")

    @classmethod
    async def update_tenant_from_property(cls, property_id: str, tenant_email: str, updated_tenant: dict):
        property = None
        try:
            property = await cls.db.properties.find_one({"_id": ObjectId(property_id)})
        except:
            raise HTTPException(400, "Please give proper ObjectId")
        
        if not property:
            raise HTTPException(404, "Property not found")
        
        tenants = property.get("tenants", [])
        for i, tenant in enumerate(tenants):
            if str(tenant.get("email")) == tenant_email:
                tenants[i] = updated_tenant
                property["tenants"] = tenants
                property_dict = PropertySchema(**property).dict()
                result = await cls.db.properties.replace_one(
                    {"_id": ObjectId(property_id)}, property_dict
                )
                if result.modified_count == 0:
                    raise HTTPException(304, "Tenant not modified")
                return property_dict
        return None

    @classmethod
    async def get_all_tenants(cls, email: Optional[str] = None):
        match_query = {}
        if email:
            match_query["tenants.email"] = email

        tenant_aggregate_query = [
            {"$unwind": "$tenants"},
            {"$match": match_query},
            {"$project": {
                "name": "$tenants.name",
                "email": "$tenants.email",
                "phone": "$tenants.phone",
                "lease_start": "$tenants.lease_start",
                "lease_end": "$tenants.lease_end",
                "property_id": "$_id",
                "property_title": "$title"
            }},
            {"$sort": {"name": 1}}
        ]

        tenants = []
        async for tenant in cls.db.properties.aggregate(tenant_aggregate_query):
            tenant["_id"] = str(tenant["_id"])
            tenant["property_id"] = str(tenant["property_id"])
            tenants.append(TenantSchema(**tenant))

        return tenants


