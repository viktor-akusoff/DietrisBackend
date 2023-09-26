from itertools import islice
from transliterate import slugify
from food.models import FoodItem
from .data_types import NutritionTable
from .load_strategy import Strategy
from typing import Set


def check_repeat(s: Set, c: str | None) -> bool:
    if c in s:
        return True
    s.add(c)
    return False


class NutritionTableContext():

    def __init__(self, strategy: Strategy) -> None:
        self._table: NutritionTable = []
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def load_table(self, file_address: str):
        self._table = self._strategy.load(file_address)

    def load_table_to_db(self):
        batch_size = 100
        cr = set(FoodItem.objects.all().values_list('slug', flat=True))
        data_to_upload = (
            FoodItem(
                name=element.name,
                slug=slugify(element.name),
                protein_per_100g=element.protein,
                fats_per_100g=element.fats,
                carb_per_100g=element.carb,
                calories_per_100g=element.calories
            ) for element in self._table if not check_repeat(cr, slugify(element.name))
        )
        while True:
            batch = list(islice(data_to_upload, batch_size))
            if not batch:
                break
            FoodItem.objects.bulk_create(batch, batch_size)
