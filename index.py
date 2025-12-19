"""Notes App - Main Application Entry Point.

A FastAPI application for creating and managing notes with MongoDB.
"""

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from routes.note import note

# Load environment variables
load_dotenv()

# Application metadata
APP_NAME = os.getenv("APP_NAME", "Notes App")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Create FastAPI application
app = FastAPI(
    title=APP_NAME,
    description="A modern notes application with FastAPI and MongoDB",
    version="1.0.0",
    debug=DEBUG
)

# Add CORS middleware (configure according to your needs)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(note)


@app.on_event("startup")
async def startup_event():
    """Application startup event handler."""
    print(f"🚀 {APP_NAME} is starting up...")
    print(f"📝 Debug mode: {DEBUG}")


@app.on_event("shutdown")
async def shutdown_event():
    """Application shutdown event handler."""
    print(f"👋 {APP_NAME} is shutting down...")


if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    
    uvicorn.run(
        "index:app",
        host=host,
        port=port,
        reload=DEBUG
    )
