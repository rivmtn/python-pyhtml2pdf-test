from pyhtml2pdf import converter

source_html_path = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\contract.html'

target_pdf_path = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\contract.pdf'


converter.convert(
    source=source_html_path,
    target=target_pdf_path,
)
