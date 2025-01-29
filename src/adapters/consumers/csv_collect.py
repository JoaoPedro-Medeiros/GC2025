from src.domain.entities.csv_table import CSVTable
from src.domain.interfaces.csv_consumer import ICSV_Consumer

class CsvOrExcelCollect(ICSV_Consumer):
    def get_table(self, pdf):
        table = CSVTable(pdf)
        return table.get_extracted_table()