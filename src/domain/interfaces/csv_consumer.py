from abc import ABC, abstractmethod
from src.domain.entities.csv_table import CSVTable

class ICSV_Consumer(ABC):
    @abstractmethod
    def get_table(self, csv_or_excel:str) -> (CSVTable | None):
        pass