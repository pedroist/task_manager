from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .db.session import engine
from .models.base import Base
from .api.v1.api import api_router

def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # Set up CORS middleware
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, replace with actual origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include the API router
    application.include_router(api_router, prefix=settings.API_V1_STR)

    return application

app = create_application()

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to Task Management API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}