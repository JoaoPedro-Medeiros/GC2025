import os.path
from PyPDF2 import PdfReader as Reader

class PDFAttributes:
    def __init__(self, pdf:str):
        self.__filepath = os.path.abspath(pdf)
        self.__pags = 0
        self.__fullpages = []
    
    def get_from_file(self, return_class:bool = True):
        with open(self.__filepath, 'rb') as file:
            pdf_reader = Reader(file)
            self.__pags = pdf_reader._get_num_pages()
            if self.__pags >= 4: # [Capa, Sumário, Capa de capítulo, Fundo padrão, restante eliminado...]
                for pag in range(4):
                    self.__fullpages.append(pdf_reader.pages[pag])
            else:
                raise Exception("Invalid PDF")
        if return_class:
            return self
    
    def get_filepath(self):
        return self.__filepath
    
    def get_number_of_pages(self):
        return self.__pags
    
    def get_fullpages(self):
        return self.__fullpages
    
    def get_all(self):
        return {
            "Caminho do Arquivo":self.__filepath,
            "Páginas do Arquivo":self.__fullpages,
            "Número de Páginas":self.__pags
        }