import os
import tempfile
from typing import Optional

from PyPDF2 import PdfFileMerger
from pyhtml2pdf import converter

from v1.config import SOURCE_HTML_PATH, TARGET_PDF_PATH, S3_PREFIX, S3_BUCKET_NAME, S3_REGION_NAME, EXTRA_PDF_PATH, \
    MERGED_PDF_PATH
from v1.storage import s3


def generate_contract_pdf(
        contract_id: Optional[str] = "unknown",

        company_name: Optional[str] = "",
        company_address: Optional[str] = "",
        date: Optional[str] = "",

        title: Optional[str] = "",
        location_name: Optional[str] = "",
        farm_name: Optional[str] = "",
        first_name: Optional[str] = "",
        last_name: Optional[str] = "",
        english_name: Optional[str] = "",
        gender: Optional[str] = "",
        birth_date: Optional[str] = "",
        cell_phone: Optional[str] = "",
        email: Optional[str] = "",
        address: Optional[str] = "",
        tax_file_number: Optional[str] = "",
        visa_grant_number: Optional[str] = "",
        visa_expiry_date: Optional[str] = "",
        nationality: Optional[str] = "",
        passport_number: Optional[str] = "",
        emergency_contact_name: Optional[str] = "",
        emergency_contact_cell_phone: Optional[str] = "",
        fund_name: Optional[str] = "",
        member_number: Optional[str] = "",
        bank_name: Optional[str] = "",
        account_name: Optional[str] = "",
        bsb: Optional[str] = "",
        account_number: Optional[str] = "",

        pre_existing_medical_condition: Optional[str] = "",
        taking_medication: Optional[str] = "",
        recent_surgery: Optional[str] = "",
        recent_injury: Optional[str] = "",
        job_related_limitation: Optional[str] = "",

        job_stress: Optional[str] = "",
        mental_counseling: Optional[str] = "",
        aware_of_eap: Optional[str] = "",

        aware_of_safety_policy: Optional[str] = "",
        first_aid_training: Optional[str] = "",
        safety_reporting_comfort: Optional[str] = "",

        bee_sting: Optional[str] = "",
        epilepsy: Optional[str] = "",
        diabetes: Optional[str] = "",
        pregnant: Optional[str] = "",
        high_blood_pressure: Optional[str] = "",
        other: Optional[str] = "",

        extra_disclosure: Optional[str] = "",

):
    with open(SOURCE_HTML_PATH, 'r', encoding='utf-8') as file:
        html_content = file.read()

    modified_html_content = (
        html_content
        .replace('COMPANY_NAME', company_name)
        .replace('COMPANY_ADDRESS', company_address)
        .replace('DATE', date)
        .replace({'Mr': 'MR_CHECKED',
                  'Mrs': 'MRS_CHECKED',
                  'Miss': 'MISS_CHECKED',
                  'Ms': 'MS_CHECKED'}.get(title, 'NOT_CHECKED'), 'checked')
        .replace('LOCATION_NAME', location_name)
        .replace('FARM_NAME', farm_name)
        .replace('FIRST_NAME', first_name)
        .replace('LAST_NAME', last_name)
        .replace('ENGLISH_NAME', english_name)
        .replace({'male': 'MALE_CHECKED',
                  'female': 'FEMALE_CHECKED'}.get(gender, 'NOT_CHECKED'), 'checked')
        .replace('BIRTH_DAY', birth_date)
        .replace('CELL_PHONE', cell_phone)
        .replace('EMAIL', email)
        .replace('ADDRESS', address)
        .replace('TAX_FILE_NUMBER', tax_file_number)
        .replace('VISA_GRANT_NUMBER', visa_grant_number)
        .replace('VISA_EXPIRY_DAY', visa_expiry_date)
        .replace('NATIONALITY', nationality)
        .replace('PASSPORT_NUMBER', passport_number)
        .replace('EMERGENCY_CONTACT_NAME', emergency_contact_name)
        .replace('EMERGENCY_CONTACT_PHONE', emergency_contact_cell_phone)
        .replace('FUND_NAME', fund_name)
        .replace('MEMBER_NUMBER', member_number)
        .replace('BANK_NAME', bank_name)
        .replace('ACCOUNT_NAME', account_name)
        .replace('BSB_VALUE', bsb)
        .replace('ACCOUNT_NUMBER', account_number)
        .replace('PRE_EXISTING_MEDICAL_CONDITION_Y',
                 'checked' if pre_existing_medical_condition == "Y" else '')
        .replace('PRE_EXISTING_MEDICAL_CONDITION_N',
                 'checked' if pre_existing_medical_condition == "N" else '')
        .replace('TAKING_MEDICATION_Y',
                 'checked' if taking_medication == "Y" else '')
        .replace('TAKING_MEDICATION_N',
                 'checked' if taking_medication == "N" else '')
        .replace('RECENT_SURGERY_Y',
                 'checked' if recent_surgery == "Y" else '')
        .replace('RECENT_SURGERY_N',
                 'checked' if recent_surgery == "N" else '')
        .replace('RECENT_INJURY_Y',
                 'checked' if recent_injury == "Y" else '')
        .replace('RECENT_INJURY_N',
                 'checked' if recent_injury == "N" else '')
        .replace('JOB_RELATED_LIMITATION_Y',
                 'checked' if job_related_limitation == "Y" else '')
        .replace('JOB_RELATED_LIMITATION_N',
                 'checked' if job_related_limitation == "N" else '')
        .replace('JOB_STRESS_Y',
                 'checked' if job_stress == "Y" else '')
        .replace('JOB_STRESS_N',
                 'checked' if job_stress == "N" else '')
        .replace('MENTAL_COUNSELING_Y',
                 'checked' if mental_counseling == "Y" else '')
        .replace('MENTAL_COUNSELING_N',
                 'checked' if mental_counseling == "N" else '')
        .replace('AWARE_OF_EAP_Y',
                 'checked' if aware_of_eap == "Y" else '')
        .replace('AWARE_OF_EAP_N',
                 'checked' if aware_of_eap == "N" else '')
        .replace('AWARE_OF_SAFETY_POLICY_Y',
                 'checked' if aware_of_safety_policy == "Y" else '')
        .replace('AWARE_OF_SAFETY_POLICY_N',
                 'checked' if aware_of_safety_policy == "N" else '')
        .replace('FIRST_AID_TRAINING_Y',
                 'checked' if first_aid_training == "Y" else '')
        .replace('FIRST_AID_TRAINING_N',
                 'checked' if first_aid_training == "N" else '')
        .replace('SAFETY_REPORTING_COMFORT_Y',
                 'checked' if safety_reporting_comfort == "Y" else '')
        .replace('SAFETY_REPORTING_COMFORT_N',
                 'checked' if safety_reporting_comfort == "N" else '')
        .replace('BEE_STING_Y',
                 'checked' if bee_sting == "Y" else '')
        .replace('BEE_STING_N',
                 'checked' if bee_sting == "N" else '')
        .replace('EPILEPSY_Y',
                 'checked' if epilepsy == "Y" else '')
        .replace('EPILEPSY_N',
                 'checked' if epilepsy == "N" else '')
        .replace('DIABETES_Y',
                 'checked' if diabetes == "Y" else '')
        .replace('DIABETES_N',
                 'checked' if diabetes == "N" else '')
        .replace('PREGNANT_Y',
                 'checked' if pregnant == "Y" else '')
        .replace('PREGNANT_N',
                 'checked' if pregnant == "N" else '')
        .replace('HIGH_BLOOD_PRESSURE_Y',
                 'checked' if high_blood_pressure == "Y" else '')
        .replace('HIGH_BLOOD_PRESSURE_N',
                 'checked' if high_blood_pressure == "N" else '')
        .replace('OTHER', other)
        .replace('EXTRA_DISCLOSURE', extra_disclosure)

    )

    with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_file:
        temp_html_path = temp_file.name
        temp_file.write(modified_html_content.encode('utf-8'))

    converter.convert(
        source=temp_html_path,
        target=TARGET_PDF_PATH,
    )
    os.remove(temp_html_path)

    merger = PdfFileMerger()
    for pdf in [EXTRA_PDF_PATH, TARGET_PDF_PATH]:
        merger.append(
            fileobj=pdf
        )
    merger.write(MERGED_PDF_PATH)
    merger.close()
    os.remove(TARGET_PDF_PATH)

    key = S3_PREFIX + contract_id + ".pdf"
    with open(MERGED_PDF_PATH, 'rb') as file:
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=key,
            Body=file,
            ACL='public-read',
        )
    os.remove(MERGED_PDF_PATH)

    s3_object_url_address = f"https://{S3_BUCKET_NAME}.s3.{S3_REGION_NAME}.amazonaws.com/{key}"
    return s3_object_url_address


