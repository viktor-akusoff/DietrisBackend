from typing import List
from dataclasses import dataclass


@dataclass
class FoodElement():
    name: str
    protein: float
    fats: float
    carb: float
    calories: float


NutritionTable = List[FoodElement]
