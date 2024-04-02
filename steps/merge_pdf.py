from PyPDF2 import PdfFileMerger

pdf_path_1 = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\contract.pdf'

pdf_path_2 = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\Fair-Work-Information-Statement.pdf'

output_pdf_path = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\merge.pdf'

pdfs = [pdf_path_2, pdf_path_1]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(
        fileobj=pdf
    )

merger.write(output_pdf_path)
merger.close()
