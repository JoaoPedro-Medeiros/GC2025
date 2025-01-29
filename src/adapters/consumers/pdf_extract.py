from src.domain.entities.pdf_attributes import PDFAttributes
from src.domain.interfaces.pdf_consumer import IPDF_Consumer

class PdfExtracter(IPDF_Consumer):
    def get_attributes(self, pdf):
        attrs = PDFAttributes(pdf)
        return attrs.get_from_file()