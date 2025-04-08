from fastapi import FastAPI, Depends
import asyncio
import uvicorn
from .kafka.consumer import start_consumer
from .api import endpoints

app = FastAPI(title="Service A")

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
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)