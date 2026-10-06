from fastapi import APIRouter, HTTPException

import crud

from models import DestinationCreate, DestinationUpdate


router = APIRouter(
    prefix="/destinations",
    tags=["Destinations"]
)



# =========================
# CREATE
# =========================

@router.post("/")
def create_destination(data: DestinationCreate):

    destination = crud.create_destination(

        country=data.country,

        city=data.city,

        budget=data.budget,

        priority=data.priority,

        status=data.status,

        travel_date=data.travel_date,

        notes=data.notes,

        capital="",
        region="",
        currency="",
        flag=""
    )

    return destination



# =========================
# READ ALL
# =========================

@router.get("/")
def get_destinations():

    return crud.get_destinations()


# =========================
# READ ONE
# =========================

@router.get("/{destination_id}")
def get_destination(destination_id: int):

    destination = crud.get_destination(
        destination_id
    )

    if not destination:

        raise HTTPException(
            status_code=404,
            detail="Destination not found."
        )

    return destination


# =========================
# UPDATE
# =========================

@router.put("/{destination_id}")
def update_destination(
    destination_id: int,
    data: DestinationUpdate
):

    old = crud.get_destination(destination_id)

    if not old:
        raise HTTPException(
            status_code=404,
            detail="Destination not found."
        )

    destination = crud.update_destination(

        destination_id,

        data.country if data.country is not None else old["country"],

        data.city if data.city is not None else old["city"],

        data.budget if data.budget is not None else old["budget"],

        data.priority if data.priority is not None else old["priority"],

        data.status if data.status is not None else old["status"],

        data.travel_date if data.travel_date is not None else old["travel_date"],

        data.notes if data.notes is not None else old["notes"],

        old["capital"],
        old["region"],
        old["currency"],
        old["flag"]
    )

    return destination


# =========================
# DELETE
# =========================

@router.delete("/{destination_id}")
def delete_destination(
    destination_id: int
):

    deleted = crud.delete_destination(
        destination_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Destination not found."
        )

    return {
        "message":
            "Destination deleted successfully."
    }