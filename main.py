import uvicorn
from fastapi import FastAPI
from routing.bus import router as buses_router
from routing.ticket import router as tickets_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(buses_router)
app.include_router(tickets_router)

# if __name__ == "__main__":
#     uvicorn.run(app="main:app", reload=True)