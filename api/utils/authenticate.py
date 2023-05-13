from fastapi import HTTPException, Header
from config import API_KEY

async def check_api_key(api_key: str = Header(...)):
    # In this example, we'll check if the API key matches a hardcoded value
    # You can replace this with your own API key validation logic
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")