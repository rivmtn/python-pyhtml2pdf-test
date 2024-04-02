import os
import tempfile

import boto3
from pyhtml2pdf import converter

from v1.config import S3_REGION_NAME, S3_ACCESS_KEY, S3_SECRET_KEY, S3_PREFIX, S3_BUCKET_NAME

source_html_path = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\contract.html'

target_pdf_path = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\data\contract.pdf'

with open(source_html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

modified_html_content = (
    html_content
    .replace('COMPANY_NAME', 'New Company')
    .replace('LOCATION_NAME', 'Caboolture')
)

with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_file:
    temp_html_path = temp_file.name
    temp_file.write(modified_html_content.encode('utf-8'))

converter.convert(
    source=temp_html_path,  # 수정된 임시 HTML 파일 경로
    target=target_pdf_path,
)

os.remove(temp_html_path)


s3 = boto3.client(service_name='s3',
                  region_name=S3_REGION_NAME,
                  aws_access_key_id=S3_ACCESS_KEY,
                  aws_secret_access_key=S3_SECRET_KEY, )

key = S3_PREFIX + "test.pdf"

with open(target_pdf_path, 'rb') as file:
    s3.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=key,
        Body=file,
        ACL='public-read',
    )

os.remove(target_pdf_path)
