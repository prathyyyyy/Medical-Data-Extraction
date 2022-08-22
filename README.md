# Medical-Data-Extraction
- This project is to implement medical data extraction , and this project will auto classify and extract useful information from medicalcare documents.
- Implemented this project by using libraries - Pytesseract(Runs On Google Optical Character Recognition-OCR), Computer Vision, Regex, PDF2Image, Pytest.
- At first we use PDF2Image library to convert PDF into image, clean the image with Computer Vision by Adaptive Thresholding Techinique and extract useful data by using Pytesseract(OCR) and regex.
- This project works well on medicalcare documents(like extracting name, patient details, medicine) and this saves time as it reduces human work and saves time from 15 min to 2 min.

# Future Goals Regarding This Project
1. As this model works well and by using advanced Computer Vision Concept like region of intrest(ROI) we can extract data with high accuracy 
2. Using further regex we can extract more useful fields in document to get more insight and save further time.
