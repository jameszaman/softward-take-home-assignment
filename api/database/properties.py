from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from datetime import datetime
from config import MONGO_DB_NAME

from config import MONGO_URI
from ..models.properties import PropertySchema


class PropertyDB:
    client = None
    db = None

    @classmethod
    def initialize(cls):
        cls.client = AsyncIOMotorClient(str(MONGO_URI))
        cls.db = cls.client[MONGO_DB_NAME]
    
    @classmethod
    async def get_properties(cls, skip: int = 0, limit: int = 100):
        cursor = cls.db.properties.find({}, {}).skip(skip).limit(limit)
        return [PropertySchema(**property) async for property in cursor]

    @classmethod
    async def get_property(cls, id: str) -> PropertySchema:
        property = await cls.db.properties.find_one({"_id": ObjectId(id)})
        return PropertySchema(**property)

    @classmethod
    async def add_property(cls, property: PropertySchema):
        property_dict = property
        result = await cls.db.properties.insert_one(property_dict)
        return str(result.inserted_id)

    @classmethod
    async def update_property(cls, id: str, property: PropertySchema):
        property_dict = property
        property_dict["updated_at"] = datetime.utcnow()
        result = await cls.db.properties.update_one(
            {"_id": ObjectId(id)}, {"$set": property_dict}
        )
        return result.modified_count

    @classmethod
    async def delete_property(cls, id: str):
        result = await cls.db.properties.delete_one({"_id": ObjectId(id)})
        return result.deleted_count
