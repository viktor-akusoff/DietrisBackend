from abc import ABC, abstractmethod
from typing import Any
import xlrd  # type: ignore
import pylightxl as xl
from data_types import FoodElement, NutritionTable


def get_float(value: Any) -> float:
    result = 0
    try:
        result = float(value)
    except ValueError:
        pass
    return result


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
            name = str(row[0])
            protein = get_float(row[1])
            fats = get_float(row[2])
            carb = get_float(row[3])
            calories = get_float(row[4])
            self.table.append(FoodElement(name, protein, fats, carb, calories))


class LightXLStrategy(Strategy):

    def load(self, file_address: str) -> None:
        book = xl.readxl(fn=file_address)
        sheet_name = book.ws_names[0]
        first_sheet = book.ws(ws=sheet_name)
        first_sheet_rows = list(first_sheet.rows)[1:]
        for row in first_sheet_rows:
            name = str(row[0])
            protein = get_float(row[1])
            fats = get_float(row[2])
            carb = get_float(row[3])
            calories = get_float(row[4])
            self.table.append(FoodElement(name, protein, fats, carb, calories))


class XLSBStrategy(Strategy):

    def load(self, file_address: str) -> None:
        pass
