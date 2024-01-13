from fastapi import FastAPI
from routing.buses import router as buses_router

app = FastAPI()

app.include_router(buses_router)