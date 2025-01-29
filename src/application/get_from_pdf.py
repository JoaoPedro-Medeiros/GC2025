from src.domain.interfaces.pdf_consumer import IPDF_Consumer

class GetFromPdfUseCase:
    def __init__(self, consumer:IPDF_Consumer, pdf:str):
        self.__consumer = consumer
        self.pdf = pdf
    
    def consume(self):
        attrs = self.__consumer.get_attributes(self.pdf)
        return attrs