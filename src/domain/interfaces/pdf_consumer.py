from abc import ABC, abstractmethod
from src.domain.entities.pdf_attributes import PDFAttributes


class IPDF_Consumer(ABC):
    @abstractmethod
    def get_attributes(self, pdf:str) -> (PDFAttributes | None):
        pass