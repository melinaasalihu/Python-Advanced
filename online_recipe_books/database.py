import sqlite3
from models import Recipe, RecipeCreate


def create_connection():
    connection = sqlite3.connect("recipe.db")

    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            ingredients TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()



create_table()



def create_recipe(recipe: RecipeCreate) -> int:
    connection = create_connection()
    cursor = connection.cursor()
    # FIXED: Added the 3rd placeholder (?) and passed ingredients
    cursor.execute(
        "INSERT INTO recipe (name, description, ingredients) VALUES (?, ?, ?)",
        (recipe.name, recipe.description, recipe.ingredients)
    )
    connection.commit()
    recipe_id = cursor.lastrowid
    connection.close()
    return recipe_id


def read_recipes():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM recipe")
    rows = cursor.fetchall()
    connection.close()


    recipes = [
        Recipe(
            id=row["id"],
            name=row["name"],
            description=row["description"],
            ingredients=row["ingredients"]
        ) for row in rows
    ]
    return recipes



def read_recipe(recipe_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM recipe WHERE id = ?", (recipe_id,))
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return Recipe(
        id=row["id"],
        name=row["name"],
        description=row["description"],
        ingredients=row["ingredients"]
    )



def update_recipe(recipe_id: int, recipe: RecipeCreate) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE recipe SET name = ?, description = ?, ingredients = ? WHERE id = ?",
        (recipe.name, recipe.description, recipe.ingredients, recipe_id)
    )
    connection.commit()
    updated = cursor.rowcount
    connection.close()
    return updated > 0



def delete_recipe(recipe_id: int) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM recipe WHERE id = ?", (recipe_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0