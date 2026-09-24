from fastapi import FastAPI

from database import create_table

from api import router


# Create database
# and table when application starts

create_table()


app = FastAPI(

    title="TripQuest API",

    description=(
        "Travel Bucket List API "
        "using CRUD and SQLite."
    ),

    version="1.0"
)


app.include_router(router)


@app.get("/")
def home():

    return {
        "application": "TripQuest",
        "message": "API is running!"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }