from fastapi import FastAPI, HTTPException
from typing import List
import database
from models import Recipe, RecipeCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipes CRUD API"}


# Shto një recetë të re
@app.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: RecipeCreate):
    recipe_id = database.create_recipe(recipe)
    return Recipe(id=recipe_id, **recipe.model_dump())


# Merr të gjitha recetat
@app.get("/recipes/", response_model=List[Recipe])
def read_recipes():
    return database.read_recipes()


# Merr një recetë specifike sipas ID-së
@app.get("/recipes/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int):
    recipe = database.read_recipe(recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


# Përditëso një recetë
@app.put("/recipes/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: RecipeCreate):
    updated = database.update_recipe(recipe_id, recipe)
    if not updated:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return Recipe(id=recipe_id, **recipe.model_dump())


# Fshi një recetë
@app.delete("/recipes/{recipe_id}", response_model=dict)
def delete_recipe(recipe_id: int):
    deleted = database.delete_recipe(recipe_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted successfully"}
