from abc import ABCMeta, abstractmethod, abstractproperty
from typing import List, Dict, LiteralString

NutritionTable = List[Dict[str, int]]

class Strategy(ABCMeta):
    
    table: NutritionTable = []
    
    @abstractmethod
    def load(self, file_address: str) -> None:
        pass
    
class XLRDStrategy(Strategy):
    
    def load(self, file_address: str) -> None:
        pass
    
class LightXLStrategy(Strategy):
    
    def load(self, file_address: str) -> None:
        pass
    
class XLSBStrategy(Strategy):
    
    def load(self, file_address: str) -> None:
        pass