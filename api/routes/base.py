from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
router = APIRouter()

@router.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

@router.get("/health", response_description="Check the health of the app")
async def health_check():
    # Check whatever you need to check to verify the app is healthy here
    health_status = {"status": "ok"}

    return JSONResponse(content=health_status)
