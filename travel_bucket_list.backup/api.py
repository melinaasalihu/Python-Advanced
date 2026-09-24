from fastapi import APIRouter, HTTPException

import crud


router = APIRouter(
    prefix="/destinations",
    tags=["Destinations"]
)


# =========================
# CREATE
# =========================

@router.post("/")
def create_destination(data: dict):

    if not data.get("country"):
        raise HTTPException(
            status_code=400,
            detail="Country is required."
        )

    if not data.get("city"):
        raise HTTPException(
            status_code=400,
            detail="City is required."
        )

    destination = crud.create_destination(

        country=data["country"],

        city=data["city"],

        budget=data.get("budget", 0),

        priority=data.get(
            "priority",
            "Medium"
        ),

        status=data.get(
            "status",
            "Wishlist"
        ),

        travel_date=data.get(
            "travel_date",
            ""
        ),

        notes=data.get(
            "notes",
            ""
        ),

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
    data: dict
):

    old = crud.get_destination(
        destination_id
    )

    if not old:

        raise HTTPException(
            status_code=404,
            detail="Destination not found."
        )

    destination = crud.update_destination(

        destination_id,

        data.get(
            "country",
            old["country"]
        ),

        data.get(
            "city",
            old["city"]
        ),

        data.get(
            "budget",
            old["budget"]
        ),

        data.get(
            "priority",
            old["priority"]
        ),

        data.get(
            "status",
            old["status"]
        ),

        data.get(
            "travel_date",
            old["travel_date"]
        ),

        data.get(
            "notes",
            old["notes"]
        ),

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