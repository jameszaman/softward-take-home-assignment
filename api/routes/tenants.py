from typing import Optional
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from api.utils.authenticate import check_api_key
from config import API_PREFIX
from ..database.tenants import TenantDB
from ..database.properties import PropertyDB
from ..models.tenants import TenantSchema

router = APIRouter(prefix=API_PREFIX +'/tenants')

@router.get("/{property_id}/tenants", response_description="Get all tenants of a property")
async def get_all_tenants(property_id: str, api_key: str = Depends(check_api_key)):
    property = await PropertyDB.get_property(property_id)
    if not property:
        raise HTTPException(404, "Property not found")
    
    tenants = await TenantDB.get_all_tenants_from_property(property_id)
    return tenants


@router.post("/{property_id}", response_description="Add new tenant")
async def create_tenant(property_id: str, tenant: TenantSchema = Body(...), api_key: str = Depends(check_api_key)):
    property = await PropertyDB.get_property(property_id)
    if not property:
        raise HTTPException(404, "Property not found")
    tenant = jsonable_encoder(tenant)
    
    try:
        new_tenant = await TenantDB.add_tenant_to_property(property_id, tenant)
        return new_tenant
    except:
        return {"message": "Tenant with this email exists. Please provide a new tenant."}

@router.put("/{property_id}/{tenant_email}", response_description="Update existing tenant")
async def update_tenant(property_id: str, tenant_email: str, updated_tenant: TenantSchema = Body(...), api_key: str = Depends(check_api_key)):
    property = await PropertyDB.get_property(property_id)
    if not property:
        raise HTTPException(404, "Property not found")

    existing_tenant = await TenantDB.get_tenant_from_property(property_id, tenant_email)    
    if not existing_tenant:
        raise HTTPException(404, "Tenant not found")
    
    
    updated_tenant_dict = updated_tenant.dict(exclude_unset=True)
    
    updated_tenant_obj = TenantSchema(**updated_tenant_dict)
    updated_tenant_obj_dict = jsonable_encoder(updated_tenant_obj)
    await TenantDB.update_tenant_from_property(property_id, tenant_email, updated_tenant_obj_dict)

    return updated_tenant_obj


@router.delete("/{property_id}/{tenant_email}", response_description="Delete Exisiting tenant")
async def delete_tenant(property_id: str, tenant_email: str, api_key: str = Depends(check_api_key)):
    property = await PropertyDB.get_property(property_id)
    if not property:
        raise HTTPException(404, "Property not found")
    deleted_tenant = await TenantDB.delete_tenant_from_property(property_id, tenant_email)
    if not deleted_tenant:
        raise HTTPException(404, "Tenant not found")
    return deleted_tenant


@router.get("/", response_description="Get all tenants")
async def get_all_tenants(email: Optional[str] = None, api_key: str = Depends(check_api_key)):
    tenants = await TenantDB.get_all_tenants(email=email)
    if not tenants:
        raise HTTPException(404, "Tenants not found")
    return tenants