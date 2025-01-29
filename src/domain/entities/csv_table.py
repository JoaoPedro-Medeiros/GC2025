import os.path
from pandas import read_csv, read_excel

class CSVTable:
    def __init__(self, csv_or_excel:str):
        self.__filepath = os.path.abspath(csv_or_excel)
        try:
            self.__table = read_csv(csv_or_excel)
        except:
            self.__table = read_excel(csv_or_excel)
    
    def get_extracted_table(self):
        return self.__table