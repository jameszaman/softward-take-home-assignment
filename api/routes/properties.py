from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from api.utils.authenticate import check_api_key
from config import API_PREFIX
from ..database.properties import PropertyDB
from ..models.properties import PropertySchema


router = APIRouter(prefix=API_PREFIX + '/properties')

@router.post("/", response_description="Add new property")
async def create_property(property: PropertySchema = Body(...), api_key: str = Depends(check_api_key)):
    property = jsonable_encoder(property)
    new_property = await PropertyDB.add_property(property)
    return new_property


@router.get("/{id}", response_description="Get a single property")
async def read_property(id: str, api_key: str = Depends(check_api_key)):
    property = await PropertyDB.get_property(id)
    if property:
        return property
    raise HTTPException(404, "Property not found")


@router.get("/", response_description="Get all properties")
async def read_properties(skip: int = 0, limit: int = 100, api_key: str = Depends(check_api_key)):
    properties = await PropertyDB.get_properties(skip, limit)
    return properties


@router.put("/{id}", response_description="Update a property")
async def update_property_data(id: str, req: PropertySchema = Body(...), api_key: str = Depends(check_api_key)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_property = await PropertyDB.update_property(id, req)
    if updated_property:
        return updated_property
    raise HTTPException(404, "Property not found")


@router.delete("/{id}", response_description="Delete a property")
async def delete_property_data(id: str, api_key: str = Depends(check_api_key)):
    deleted_property = await PropertyDB.delete_property(id)
    if deleted_property:
        return "Property deleted successfully"
    raise HTTPException(404, "Property not found")
