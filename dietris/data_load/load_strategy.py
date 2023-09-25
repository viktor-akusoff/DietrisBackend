from abc import ABC, abstractmethod
import xlrd  # type: ignore
from data_types import FoodElement, NutritionTable


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
            row = first_sheet.row(i)
            self.table.append(FoodElement(row[0], row[1], row[2], row[3], row[4]))


class LightXLStrategy(Strategy):

    def load(self, file_address: str) -> None:
        pass


class XLSBStrategy(Strategy):

    def load(self, file_address: str) -> None:
        pass
