import sqlite3
from models import Recipe, RecipeCreate


def create_connection():
    connection = sqlite3.connect("recipe.db")
    # This allows accessing columns by name (e.g., row["name"])
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    # FIXED: Added a missing comma after 'description text not null'
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


# Initialize the table
create_table()


# FIXED: Renamed to create_recipe, fixed parameter names, SQL placeholders, and syntax
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


# FIXED: Renamed to read_recipes and mapped to the Recipe model
def read_recipes():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM recipe")
    rows = cursor.fetchall()
    connection.close()

    # Using row keys since row_factory = sqlite3.Row is enabled
    recipes = [
        Recipe(
            id=row["id"],
            name=row["name"],
            description=row["description"],
            ingredients=row["ingredients"]
        ) for row in rows
    ]
    return recipes


# FIXED: Renamed to read_recipe and fixed mapping
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


# FIXED: Renamed to update_recipe and updated SQL structure
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


# FIXED: Renamed to delete_recipe
def delete_recipe(recipe_id: int) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM recipe WHERE id = ?", (recipe_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0