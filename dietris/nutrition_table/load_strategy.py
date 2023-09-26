from abc import ABC, abstractmethod
from typing import Any
import csv
import xlrd  # type: ignore
import pylightxl as xl
from pyexcel_ods import read_data

from .load_exceptions import NutritionTableLoadError
from .data_types import FoodElement, NutritionTable


def get_float(value: Any) -> float:
    result = 0
    try:
        result = float(value)
    except ValueError:
        pass
    return result


class Strategy(ABC):

    _table: NutritionTable = []

    @abstractmethod
    def load(self, file_address: str) -> NutritionTable:
        pass


class XLSStrategy(Strategy):

    def load(self, file_address: str) -> NutritionTable:
        try:
            book = xlrd.open_workbook(file_address)
        except Exception:
            raise NutritionTableLoadError('Incorrect xls file.')
        first_sheet = book.sheet_by_index(0)
        for i in range(1, first_sheet.nrows):
            row = first_sheet.row(i)
            name = str(row[0].value)
            protein = get_float(row[1].value)
            fats = get_float(row[2].value)
            carb = get_float(row[3].value)
            calories = get_float(row[4].value)
            self._table.append(FoodElement(name, protein, fats, carb, calories))
        return self._table


class XLSXStrategy(Strategy):

    def load(self, file_address: str) -> NutritionTable:
        try:
            book = xl.readxl(fn=file_address)
        except Exception:
            raise NutritionTableLoadError('Incorrect xlsx file.')
        sheet_name = book.ws_names[0]
        first_sheet = book.ws(ws=sheet_name)
        first_sheet_rows = list(first_sheet.rows)[1:]
        for row in first_sheet_rows:
            name = str(row[0])
            protein = get_float(row[1])
            fats = get_float(row[2])
            carb = get_float(row[3])
            calories = get_float(row[4])
            self._table.append(FoodElement(name, protein, fats, carb, calories))
        return self._table


class CSVStrategy(Strategy):

    def load(self, file_address: str) -> NutritionTable:
        try:
            with open(file_address, encoding='utf-8') as book:
                reader = csv.reader(book, delimiter=';')
                for row in reader:
                    name = str(row[0])
                    protein = get_float(row[1].replace(',', '.'))
                    fats = get_float(row[2].replace(',', '.'))
                    carb = get_float(row[3].replace(',', '.'))
                    calories = get_float(row[4].replace(',', '.'))
                    self._table.append(FoodElement(name, protein, fats, carb, calories))
        except Exception:
            raise NutritionTableLoadError('Incorrect csv file.')
        return self._table


class ODSStrategy(Strategy):

    def load(self, file_address: str) -> NutritionTable:
        try:
            book_dict = read_data(file_address)
        except Exception:
            raise NutritionTableLoadError('Incorrect ods file.')
        book = book_dict.popitem()[1][1:]
        for row in book:
            if not row:
                continue
            name = str(row[0])
            protein = get_float(row[1])
            fats = get_float(row[2])
            carb = get_float(row[3])
            calories = get_float(row[4])
            self._table.append(FoodElement(name, protein, fats, carb, calories))
        return self._table
