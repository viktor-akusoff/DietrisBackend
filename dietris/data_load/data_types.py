from typing import List
from dataclasses import dataclass


@dataclass
class FoodElement():
    name: str
    protein: float
    fats: float
    carb: float
    callories: float


NutritionTable = List[FoodElement]
