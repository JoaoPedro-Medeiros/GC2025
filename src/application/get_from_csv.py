from src.domain.interfaces.csv_consumer import ICSV_Consumer

class GetFromCsvOrExcelUseCase:
    def __init__(self, consumer:ICSV_Consumer, csv_or_excel:str):
        self.__consumer = consumer
        self.csv_or_excel = csv_or_excel
    
    def consume(self):
        price_table = self.__consumer.get_table(self.csv_or_excel)
        return price_table