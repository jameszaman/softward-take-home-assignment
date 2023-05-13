from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import base, tenants, properties
from api.database.connector import db

from api.database.properties import PropertyDB
from api.database.tenants import TenantDB

app = FastAPI()

PropertyDB.initialize()
TenantDB.initialize()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routes
app.include_router(base.router)
app.include_router(properties.router)
app.include_router(tenants.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
