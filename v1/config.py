import os

from dotenv import load_dotenv

SOURCE_HTML_PATH = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\v1\contract.html'
EXTRA_PDF_PATH = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\v1\Fair-Work-Information-Statement.pdf'
TARGET_PDF_PATH = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\v1\contract.pdf'
MERGED_PDF_PATH = r'C:\Users\newyork\PycharmProjects\pythonPdfTest\v1\merged.pdf'

load_dotenv()

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_REGION_NAME = os.getenv("S3_REGION_NAME")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_PREFIX = os.getenv("S3_PREFIX")
