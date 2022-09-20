import pytesseract
from pdf2image import convert_from_path
import utility
from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPULAR_PATH = r'C:\poppler-22.04.0\Library\bin'


def extract(filepath, fileformat):
    # Extract PDF file
    pages = convert_from_path(filepath, poppler_path=POPULAR_PATH)
    document_text = ""

    if len(pages)>0:
        page = pages[0]
        processed_image = utility.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    # Extract Field From Text
    if fileformat == "prescription":
        extracted_data = PrescriptionParser(document_text).parse()

    elif fileformat == "patient_details":
       extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid Document Format:{fileformat}")

    return extracted_data



if __name__ == "__main__":
    data = extract("..\Documents\prescription\pre_2.pdf","prescription")
    print(data)
