from pydantic import BaseModel

# Kjo përdoret kur krijojmë një recetë të re (nuk e dimë ID-në ende)
class RecipeCreate(BaseModel):
    name: str
    description: str
    ingredients: str

# Kjo përdoret kur kthejmë recetën nga databaza (përfshin edhe ID-në)
class Recipe(RecipeCreate):
    id: int