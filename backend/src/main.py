from fastapi import FastAPI,Form,UploadFile,File
import uvicorn
from extractor import extract
import uuid
import os


app = FastAPI()

@app.post("/extract_from_doc")
def extract_from_doc(file_format:str=Form(),file:UploadFile=File()):
    contents =file.file.read()    # Read The Content In The File
    file_path = "../upload/" + str(uuid.uuid4()) + ".pdf"   #universally unique identifier -Gives unique str To Avoid Overriding During Multiple Host Calling Server
    with open(file_path,"wb") as f:   # Wb is Write Byte As It Stores In Bytes
        f.write(contents)
    try:
        data = extract(file_path,file_format)
    except Exception as e:
        data = {
            "error":str(e)
        }
    if os.path.exists(file_path):
        os.remove(file_path)
    return data
if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)