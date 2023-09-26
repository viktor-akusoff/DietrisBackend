from .data_types import NutritionTable
from .load_strategy import Strategy


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
        pass
