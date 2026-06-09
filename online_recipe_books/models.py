from pydantic import BaseModel


class RecipeCreate(BaseModel):
    name: str
    description: str
    ingredients: str


class Recipe(RecipeCreate):
    id: int