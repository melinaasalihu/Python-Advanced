import sqlite3

from database import get_connection




def create_destination(
    country,
    city,
    budget,
    priority,
    status,
    travel_date,
    notes,
    capital,
    region,
    currency,
    flag
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO destinations
        (
            country,
            city,
            budget,
            priority,
            status,
            travel_date,
            notes,
            capital,
            region,
            currency,
            flag
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        country,
        city,
        budget,
        priority,
        status,
        travel_date,
        notes,
        capital,
        region,
        currency,
        flag
    ))

    connection.commit()

    new_id = cursor.lastrowid

    connection.close()

    return get_destination(new_id)



def get_destinations():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM destinations
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]




def get_destination(destination_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM destinations
        WHERE id = ?
    """, (destination_id,))

    row = cursor.fetchone()

    connection.close()

    if row:
        return dict(row)

    return None



def update_destination(
    destination_id,
    country,
    city,
    budget,
    priority,
    status,
    travel_date,
    notes,
    capital,
    region,
    currency,
    flag
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE destinations

        SET
            country = ?,
            city = ?,
            budget = ?,
            priority = ?,
            status = ?,
            travel_date = ?,
            notes = ?,
            capital = ?,
            region = ?,
            currency = ?,
            flag = ?

        WHERE id = ?
    """, (
        country,
        city,
        budget,
        priority,
        status,
        travel_date,
        notes,
        capital,
        region,
        currency,
        flag,
        destination_id
    ))

    connection.commit()

    connection.close()

    return get_destination(destination_id)



def delete_destination(destination_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM destinations
        WHERE id = ?
    """, (destination_id,))

    connection.commit()

    deleted = cursor.rowcount > 0

    connection.close()

    return deleted