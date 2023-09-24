from abc import ABC, abstractmethod
from typing import List, Dict, Union
import xlrd  # type: ignore

NutritionData = Dict[str, Union[str, int]]
NutritionTable = List[NutritionData]


class Strategy(ABC):

    table: NutritionTable = []

    @abstractmethod
    def load(self, file_address: str) -> None:
        pass


class XLRDStrategy(Strategy):

    def load(self, file_address: str) -> None:
        book = xlrd.open_workbook(file_address)
        first_sheet = book.sheet_by_index(0)
        for i in range(1, first_sheet.nrows):
            self.table.append(
                {
                    'name': first_sheet.cell_value(rowx=i, colx=0),
                    'protein': first_sheet.cell_value(rowx=i, colx=1),
                    'fats': first_sheet.cell_value(rowx=i, colx=2),
                    'carb': first_sheet.cell_value(rowx=i, colx=3),
                    'callories': first_sheet.cell_value(rowx=i, colx=4)
                }
            )


class LightXLStrategy(Strategy):

    def load(self, file_address: str) -> None:
        pass


class XLSBStrategy(Strategy):

    def load(self, file_address: str) -> None:
        pass
