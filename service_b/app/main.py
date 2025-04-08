from fastapi import FastAPI, Depends
import asyncio
import uvicorn
from .kafka.consumer import start_consumer
from .api import endpoints
from .config import settings

app = FastAPI(title=settings.SERVICE_NAME)

# Include API routes
app.include_router(endpoints.router)

@app.on_event("startup")
async def startup_event():
    # Start Kafka consumer in the background
    asyncio.create_task(start_consumer())

@app.on_event("shutdown")
async def shutdown_event():
    # Add any cleanup code here
    pass

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.API_PORT, reload=True)