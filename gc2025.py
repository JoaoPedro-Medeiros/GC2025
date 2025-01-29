import sys, pandas as pd
from src.adapters.consumers.pdf_extract import PdfExtracter
from src.application.get_from_pdf import GetFromPdfUseCase
from src.infrastructure.logging.logging_config import setup_logging
from src.adapters.consumers.csv_collect import CsvOrExcelCollect
from src.application.get_from_csv import GetFromCsvOrExcelUseCase
import logging

if __name__ == '__main__':
    try:
        arg1 = sys.argv[0]
        arg2 = sys.argv[1]
    except:
        arg1 = input("PDF Filepath: ")
        arg2 = input("CSV or Excel Filepath: ")
else :
    arg1 = sys.argv[0]
    arg2 = sys.argv[1]

extracter = PdfExtracter()
collecter = CsvOrExcelCollect()

get_from_pdf = GetFromPdfUseCase(extracter, arg1)
get_from_csv = GetFromCsvOrExcelUseCase(collecter, arg2)
pdf_attrs = get_from_pdf.consume()
complete_csv = get_from_csv.consume()

print(pdf_attrs.get_all())
print(complete_csv.head())

#TODO Continuar daqui --> Corrigir valores do leitor de PDF