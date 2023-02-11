# Medical Data Extraction : 

![](https://media1.giphy.com/media/zUxhmejE6KnrdgV6RN/giphy.gif?cid=ecf05e47cvfd41w4cvjw0zow19mqa8h8inqpx63cyjxc5wlc&rid=giphy.gif&ct=g)

## 1. Introduction :

- This project is to implement medical data extraction , and this project will auto classify and extract useful information from medicalcare documents.
- Implemented this project by using libraries - Pytesseract(Runs On Google Optical Character Recognition-OCR), Computer Vision, Regex, PDF2Image, Pytest.
- At first we use PDF2Image library to convert PDF into image, clean the image with Computer Vision by Adaptive Thresholding Techinique and extract useful data by using Pytesseract(OCR) and regex.
- This project works well on medicalcare documents(like extracting name, patient details, medicine) and this saves time as it reduces human work and saves time from 15 min to 2 min.

## 2. Major Libraries and tools : 

* Pdf2image - This library is used in this project to convert medical document pdf file to text 
* openCV - This library is used in this project for processing and cleaning the image by adaptive threshold method.
* pytesseract - This library is used in this project for converting image containing useful information to text and this library runs on google optical character recognition engine (OCR). 
* regex - This library is used in this project for extracting useful and required text from text data .
* Pytest - This library is used in this project to perform effective testing . 

## 3. Project workflow : 
- Documents : Sample data used in this project - [https://github.com/prathyyyyy/Medical-Data-Extraction/tree/main/document_extractor/Documents].
- Source code : Major files - [https://github.com/prathyyyyy/Medical-Data-Extraction/tree/main/document_extractor/src].
- Test files - [https://github.com/prathyyyyy/Medical-Data-Extraction/tree/main/document_extractor/tests].
- Minor files : These are minor files and notebook for learning about dataset - [https://github.com/prathyyyyy/Medical-Data-Extraction/tree/main/document_extractor/Notebook].

## 4. Project tasks : 
1. Collect and dataset.
2. Analyse the data and get useful insights from data .
3. Use pdf2image to convert pdf to image.
4. use computer vision (opencv) to process and clean the image by adaptive thresholding technique.
5. By pyteserract (OCR) convert the processed and clean image to extract the data . 
6. By Regular expression (RE) extract useful information from the extracted text data.
7. By pytest test the project and quality of code .

## 5. Future Goals Regarding This Project : 
1. As this model works well and by using advanced Computer Vision Concept like region of intrest(ROI) we can extract data with high accuracy 
2. Using further regex we can extract more useful fields in document to get more insight and save further time.
