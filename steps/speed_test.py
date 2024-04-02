import time

import pdfkit
from pyhtml2pdf import converter

source_html_path = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\contract.html'

target_pdf_path = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\contract.pdf'


def pdfkit_convert():
    start = time.time()
    pdfkit.from_file(
        input=source_html_path,
        output_path=target_pdf_path,
        options={
            'page-size': 'A4',
            'margin-top': '0in',
            'margin-right': '0in',
            'margin-bottom': '0in',
            'margin-left': '0in',
            'encoding': "UTF-8",
        },
    )
    end = time.time()
    print(end - start)


def pyhtml2pdf_convert():
    start = time.time()
    converter.convert(
        source=source_html_path,
        target=target_pdf_path,
    )
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    pdfkit_convert()
    # pyhtml2pdf_convert()
