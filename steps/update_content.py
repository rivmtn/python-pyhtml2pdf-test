import os
import tempfile

from pyhtml2pdf import converter

source_html_path = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\contract.html'

target_pdf_path = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\contract.pdf'

# HTML 파일을 읽기
with open(source_html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# HTML 내용 수정하기 (예: 'old_value'를 'new_value'로 변경)
modified_html_content = (
    html_content
    .replace('COMPANY_NAME', 'New Company')
    .replace('LOCATION_NAME', 'Caboolture')
)

# 수정된 HTML 내용을 임시 파일로 저장
with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_file:
    temp_html_path = temp_file.name
    temp_file.write(modified_html_content.encode('utf-8'))

# PDF 변환
converter.convert(
    source=temp_html_path,  # 수정된 임시 HTML 파일 경로
    target=target_pdf_path,
)

# 임시 HTML 파일 삭제
os.remove(temp_html_path)
